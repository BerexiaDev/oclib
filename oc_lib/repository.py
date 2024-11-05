from oc_lib.db import db
from oc_lib.utils.exceptions import DateValidationError

from sqlalchemy import desc, func
from copy import deepcopy


class Repository:

    def to_dict(self):
        full_dict = deepcopy(self.__dict__)
        full_dict.pop('_sa_instance_state')
        return full_dict

    @classmethod
    def create(cls, **kwargs):
        """Create a new object and save it to the database"""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update an object with new values and save it to the database"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        if commit:
            self.save()
        return self

    def delete(self, commit=True):
        """Delete an object from the database"""
        try:
            db.session.delete(self)
            if commit:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def delete_all(cls):
        """Delete all rows from a table in the database."""
        try:
            db.session.query(cls).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)
        
    def rollack(self):
        db.session.rollback()

    @classmethod
    def find_one(cls, **kwargs):
        """Find the first object that matches the given filters"""
        try:
            return cls.query.filter_by(**kwargs).first()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def child_count(cls, **kwargs):
        """Check using func count that parent got children without loading records"""
        try:
            # Build the exists query with filter conditions from kwargs
            return db.session.query(func.count(cls.id)).filter_by(**kwargs).scalar()

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def get_last_inserted(cls):
        """Get the last inserted object"""
        try:
            return cls.query.order_by(cls.id.desc()).first()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def get_last_filtered_insert(cls, **kwargs):
        """Get the last inserted object with filters"""
        try:
            return cls.query.filter_by(**kwargs).order_by(cls.id.desc()).first()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)
    
    @classmethod
    def get_before_last_filtered(cls, **kwargs):
        """Get the second-to-last inserted object with filters"""
        try:
            return cls.query.filter_by(**kwargs).order_by(cls.id.desc()).offset(1).first()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def find_all(cls, **kwargs):
        """Find all objects that match the given filters"""
        try:
            return cls.query.filter_by(**kwargs).all()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def dynamic_find_all(self, table_name, distinct=False, select=None, **kwargs):
        try:
            table = db.Model.metadata.tables.get(table_name)
            if table is None:
                raise ValueError(f"Table '{table_name}' not found")

            query = db.session.query(table)

            if distinct:
                query = query.distinct()

            if select:
                query = query.with_entities(*select)

            for key, value in kwargs.items():
                query = query.filter(getattr(table.columns, key) == value)
            return query.all()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @classmethod
    def receive_before_insert(cls,ep_id):
        filters = {}
        if ep_id:   #it means we are calculating mandataire sequence for specific Ep
            filters.update({'ep_id': ep_id})
        obj = cls.query.filter_by(**filters).order_by(desc(cls.sequence_number)).first()
        if obj is None or obj.sequence_number is None:
            return 1

        return obj.sequence_number + 1

    def save(self, commit=True, apply_before_insert=False, ep_id=None):
        """Save an object to the database"""
        if apply_before_insert:
            self.sequence_number = self.receive_before_insert(ep_id)

        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except DateValidationError as e:
                db.session.rollback()
                raise DateValidationError(e)
            except Exception as e:
                db.session.rollback()
                # return False
                raise Exception(e)
            finally:
                db.session.expire_all()
            db.session.refresh(self)
        return self

    @classmethod
    def bulk_save(cls, objects, commit=True):
        """
        Save multiple objects to the database in bulk.
        """
        try:
            # Add all objects to the session in bulk
            db.session.bulk_save_objects(objects)
            
            if commit:
                db.session.commit()
            
            return True  # Return True to indicate success
        except Exception as e:
            db.session.rollback()  # Rollback if something goes wrong
            raise Exception(f"Error in bulk saving objects: {e}")

    @classmethod
    def bulk_update(self, objects, commit=True):
        """
        Update multiple objects in the database in bulk.
        """
        try:
            # Update all objects in the session in bulk
            db.session.bulk_update_mappings(objects)

            if commit:
                db.session.commit()

            return True  # Return True to indicate success
        except Exception as e:
            db.session.rollback()