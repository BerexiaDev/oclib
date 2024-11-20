from oc_lib.utils.constants import Roles, QUALITE_BENEFICIAIRE_MAPPING, CATEGORIE_PC_MAPPING, STATUT_MAPPING, \
    YES_NO_MAPPING, CREATION_STATUS_MAPPING, Type_Operation_MAPPING, PM_TYPE_MAPPING, ROLES_MAPPING
from oc_lib.utils.export_table_data_func import get_designation_agence, get_poc_id, get_pp_field_name, \
    get_lieu_implantation_label, get_categorie_op, get_pm_id, get_affiliation_group, get_apa_actif, \
    get_m_actif, get_ama_actif, get_pm, get_poc, get_motif, get_valide_manager_oc, get_numero_agrement, \
    get_pattern, get_sous_operation_code, get_sous_operation_code_statistique, get_sous_operation_label, \
    get_sous_operation_lieu_implantations, get_payment_method, get_operator_pm, get_derogration_op, \
    get_latence_jours, get_nature_beneficiaire, get_delai, get_only_date, get_cin, get_passport, \
    get_lieu_implantation_label_for_poc, get_beneficiaire_pm_qualite, get_beneficiaire_pm_field_value, \
    get_beneficiaire_pp_qualite, get_beneficiaire_pp_field_value

EXPORT_TABLE_INFO = {
    "operation_achat_view": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.PREPOSE.value, Roles.OP.value],
        "func_path": "app.main.services.operation_achat_service",
        "func_name": "get_all_operation_achats",
        "values_mapping": {
            "statut": STATUT_MAPPING,
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "beneficiaire_pp_qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "beneficiaire_pc_qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "beneficiaire_pm_qualite": QUALITE_BENEFICIAIRE_MAPPING,
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",
            "numero_bordereau": "Numéro Bordereau",
            "date_bordereau": "Date & Heure Bordereau",

            "categorie_op": "Catégorie PM",
            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "categorie_pc": "Catégorie Point de change",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "poc_adresse": "Poc adresse",
            "created_by": "Préposé",
            "date_creation": "Date de création",
            "beneficiaire_pm_qualite": "Qualité Client/Bénéficiaire PM",
            "beneficiaire_pp_qualite": "Qualité Client/Bénéficiaire PP",
            "sous_operation_label": "Sous operation label",
            "sous_operation_id": "Sous operation ID",
            "beneficiaire_pp_id": "Beneficiaire pp ID",
            "beneficiaire_pp_nature_piece": "Nature de la pièce d’identité",
            "beneficiaire_pp_numero_piece": "Numéro de la pièce d’identité",
            "beneficiaire_pp_nom": "Nom bénéficiaire",
            "beneficiaire_pp_prenom": "Prénom bénéficiaire",
            "beneficiaire_pp_nationalite": "Nationalité du client/Pays d’accueil",
            "beneficiaire_pm_id": "Beneficiaire pm ID",
            "beneficiaire_pm_registre_commerce": "RC",
            "beneficiaire_pm_centre": "Centre",
            "beneficiaire_pm_raison_sociale": "Raison sociale",
            "beneficiaire_pm_idce": "ICE",
            "numero_declaration": "Numéro de la déclaration d’importation des devises billets de banque",
            "date_declaration": "Date de la déclaration d’importation des devises billets de banque",
            "statut": "Statut",
            "devise_labels": "Devises",
            "montant_global": "Montant Global en MAD",
            "support_mad": "Support MAD",

            "beneficiaire_pc_qualite": "Qualité Client/Bénéficiaire PC",
            "beneficiaire_pc_numero_agrement": "Numéro agrément",
            "beneficiaire_pc_nom_agence": "Dénomination PC",
            "cancelled_by": "Annulé par",
            "date_cancellation": "Date d'annulation",
            "cancellation_reason": "Motif d'annulation",
            "pm": {
                "title": "Opérateur",
                "func": get_pm
            },
            "poc": {
                "title": "Point de change",
                "func": get_poc
            }
        }
    },
    "operation_vente_view": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.PREPOSE.value, Roles.OP.value],
        "func_path": "app.main.services.operation_vente_service",
        "func_name": "get_all_operation_ventes",
        "values_mapping": {
            "statut": STATUT_MAPPING,
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "beneficiaire_pp_qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "beneficiaire_final_pp_qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "beneficiaire_pc_qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "beneficiaire_pm_qualite": QUALITE_BENEFICIAIRE_MAPPING,
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",

            "numero_bordereau": "Numéro Bordereau",
            "date_bordereau": "Date & Heure Bordereau",
            "date_creation": "Date de création",
            "created_by": "Préposé",
            "categorie_op": "Catégorie PM",
            "categorie_pc": "Catégorie Point de change",
            "beneficiaire_pp_qualite": "Qualité Client/Bénéficiaire PP",
            "sous_operation_label": "Type d’opération",
            "beneficiaire_pp_nature_piece": "Nature de la pièce d’identité",
            "beneficiaire_pp_numero_piece": "Numéro de la pièce d’identité",
            "beneficiaire_pp_nom": "Nom bénéficiaire",
            "beneficiaire_pp_prenom": "Prénom bénéficiaire",
            "beneficiaire_final_pp_nom": "Nom bénéficiaire final",
            "beneficiaire_final_pp_prenom": "Prénom bénéficiaire final",
            "beneficiaire_final_pp_qualite": "Qualité Bénéficiaire final",
            "beneficiaire_final_pp_nature_piece": "Nature pièce d’identité – Bénéficiaire final",
            "beneficiaire_final_pp_numero_piece": "Numéro pièce d’identité – Bénéficiaire final",
            "beneficiaire_pc_qualite": "Qualité Client/Bénéficiaire PC",
            "beneficiaire_pc_numero_agrement": "Numéro agrément",
            "beneficiaire_pc_nom_agence": "Dénomination PC",
            "beneficiaire_pm_qualite": "Qualité Client/Bénéficiaire PM",
            "beneficiaire_pm_raison_sociale": "Raison sociale",
            "beneficiaire_pm_registre_commerce": "RC",
            "beneficiaire_pm_centre": "Centre",
            "numero_autorisation": "Numéro d’autorisation particulière",
            "montant_global": "Montant Global en MAD",
            "devise_labels": "Devises",
            "statut": "Statut",
            "cancelled_by": "Annulé par",
            "date_cancellation": "Date d’annulation",
            "cancellation_reason": "Motif d’annulation",

            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "poc_adresse": "Poc adresse",
            "sous_operation_id": "Sous operation ID",
            "beneficiaire_pp_id": "Beneficiaire pp ID",
            "beneficiaire_pp_nationalite": "Beneficiaire pp nationalite",
            "beneficiaire_pm_id": "Beneficiaire pm ID",
            "beneficiaire_pm_idce": "Beneficiaire pm IDCE",
            "support_mad": "Support MAD",

            "pm": {
                "title": "Opérateur",
                "func": get_pm,
            },
            "poc": {
                "title": "Point de change",
                "func": get_poc,
            }
        }
    },
    "operation_cession_view": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.PREPOSE.value, Roles.OP.value],
        "func_path": "app.main.services.operation_cession_service",
        "func_name": "get_all_operation_cessions",
        "values_mapping": {
            "statut": STATUT_MAPPING,
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "is_late": YES_NO_MAPPING,
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",

            "numero_bordereau": "Numéro Bordereau",
            "date_cession": "Date de la cession",
            "categorie_op": "Catégorie Opérateur",
            "categorie_pc": "Catégorie Point de change",
            "sous_operation_label": "Type d’opération",
            "date_creation": "Date/Heure de la saisie de cession",
            "created_by": "Préposé",
            "code_banque": "Banque ",
            "code_agence": "Agence",
            "devise_labels": "Devises",
            "montant_global": "Montant Global en MAD",
            "cancelled_by": "Annulé par",
            "date_cancellation": "Date d’annulation",
            "cancellation_reason": "Motif d’annulation",
            "is_late": "Effectuée en retard",

            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "total_devises": "Total devises",
            "statut": "Statut",

            "pm": {
                "title": "Opérateur",
                "func": get_pm
            },
            "poc": {
                "title": "Point de change",
                "func": get_poc
            },
        }
    },
    "poc": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.entity_service",
        "func_name": "get_all_pocs",
        "values_mapping": {
            "creation_status": CREATION_STATUS_MAPPING,
            "statut_activite": {
                1: 'En activité',
                2: 'Arrêt Provisoire',
                3: 'Suspension ferme',
                4: 'Suspension ouverte',
                5: 'Retiré',
                6: 'Annulé',
                7: 'En arrêt'
            },
            "statut_agrement": {
                1: 'Actif',
                2: 'Inactif',
                3: 'Néant'
            },
            "categorie": CATEGORIE_PC_MAPPING,
            "is_agrement": YES_NO_MAPPING,
            "is_permanent": YES_NO_MAPPING,
            "is_link": YES_NO_MAPPING,
        },
        "columns": {
            "id": "ID",
            "forme_juridique": "Forme Juridique",
            "is_link": "Avec liaison",
            "is_source": "Is Source",
            "motif": "Motif liaison",
            "secteur_activite": "Secteur Activite",
            "nature": "Nature",
            "nom_agence": "Désignation de l'agence",
            "adresse": "Adresse",
            "date_modification_adresse": "Date Modification Adresse",
            "localite": "Localité",
            "localite_code": "Localite Code",
            "region": "Région",
            "is_agrement": "Agrément",
            "is_permanent": "Permanent",
            "numero_agrement": "№ Agrément",
            "encaisse": "Encaisse",
            "seuil_encaisse": "Seuil Encaisse",
            "seuil_encaisse_depasse": "Seuil Encaisse Depasse",
            "flag_retablissement_agrement": "Flag Retablissement Agrement",
            "date_retablissement_agrement": "Date Retablissement Agrement",
            "date_modification_encaisse": "Date Modification Encaisse",
            "date_debut_activite": "Date début activité",
            "date_fin_activite": "Date fin activité",
            "statut_activite": "Statut activité",
            "statut_agrement": "Statut agrément",
            "raison_sociale_pm": "Raison Sociale PM",
            "creation_status": "Statut de création",
            "categorie": "Catégorie Point de change",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "mandataire_id": "Mandataire ID",
            "lieu_implantation_id": "Lieu Implantation ID",
            "linked_poc_id": "ID PC liaison",
            "numero_delivrance": "N° délivrance décision premier agrément",
            "date_delivrance": "Date délivrance décision premier agrément",
            "lieu_implantation": {
                "title": "Lieu Implantation",
                "func": get_lieu_implantation_label_for_poc
            },
            "categorie_op": {
                "title": "Catégorie Opérateur",
                "func": get_categorie_op
            },
            "pm_id": {
                "title": "PM",
                "func": get_pm_id
            }
        }
    },
    "pp": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.entity_service",
        "func_name": "get_all_pps",
        "values_mapping": {
            "statut": {
                True: "Active",
                False: "Inactive"
            },
            "type": {
                "prepose": "Préposé",
                "suppleant": "Suppléant",
                "associe_pp": "Associé",
                "representant": "Représentant",
                "gerant": "Gérant"
            }
        },
        "columns": {
            "id": "ID",
            "nom": "Nom",
            "prenom": "Prénom",
            "nature_piece": "Nature",
            "numero_piece": "Numéro Pièce",
            "nationalite": "Nationalité",
            "adresse": "Adresse",
            "email": "Email",
            "phone": "Phone",
            "nature_pp": "Nature PP",
            "date_nomination": "Date nomination",
            "date_demission": "Date démission",
            "statut": "Statut",
            "type": "Type PP",
            "nom_agence": {
                "title": "Désignation de l'agence",
                "func": get_designation_agence
            },
            "poc_id": {
                "title": "POC",
                "func": get_poc_id
            },
            "raison_sociale": {
                "title": "Raison Sociale",
                "func": get_pp_field_name
            },
            "centre": {
                "title": "Centre",
                "func": get_pp_field_name
            },
            "registre_commerce": {
                "title": "Registre de Commerce",
                "func": get_pp_field_name
            }
        }
    },
    "pm": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.entity_service",
        "func_name": "get_all_pms",
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Radiée"
            },
            "type": PM_TYPE_MAPPING,
            "creation_status": CREATION_STATUS_MAPPING,
        },
        "columns": {
            "id": "ID",
            "nature_pm": "Nature PM",
            "numero_autorisation": "Numero autorisation",
            "localite": "Localite",
            "localite_code": "Localite code",
            "region": "Region",
            "centre": "Centre",
            "ville": "Ville",
            "registre_commerce": "RC",
            "adresse": "Adresse",
            "raison_sociale": "RS",
            "idce": "ICE",
            "idf": "IF",
            "forme_juridique": "Forme Juridique",
            "capital_social": "Capital social",
            "statut": "Statut",
            "email": "E-Mail",
            "telephone": "Téléphone",
            "date_creation": "Date de creation",
            "date_radiation": "Date de radiation",
            "pays": "Pays",
            "id_pays": "ID pays",
            "type": "Type"
        }
    },
    "scd": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.scd_service",
        "func_name": "get_all_scds",
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Radiée"
            },
            "type": PM_TYPE_MAPPING,
            "creation_status": CREATION_STATUS_MAPPING,
        },
        "columns": {
            "id": "ID",
            "groupe": "Groupe",
            "motif": "Motif",
            "poc_total": "PC total",
            "poc_actif": "PC actifs",
            "poc_inactif": "PC inactifs",
            "creation_status": "Statut de création",
            "part_total": "Part Total",
            "sequence_number": "Sequence Number",
            "affiliation_group_id": "Affiliation Group ID",
            "affiliation_group_motif": "Groupe Motif",
            "numero_decision_autorisation": "Numero Decision Autorisation",
            "date_decision_autorisation": "Date Decision Autorisation",

            "nature_pm": "Nature PM",
            "numero_autorisation": "Numero autorisation",
            "localite": "Localite",
            "localite_code": "Localite code",
            "region": "Region",
            "centre": "Centre",
            "ville": "Ville",
            "registre_commerce": "RC",
            "adresse": "Adresse",
            "raison_sociale": "RS",
            "idce": "ICE",
            "idf": "IF",
            "forme_juridique": "Forme Juridique",
            "capital_social": "Capital social",
            "statut": "Statut",
            "email": "E-Mail",
            "telephone": "Telephone",
            "date_creation": "Date de creation",
            "date_radiation": "Date de radiation",
            "pays": "Pays",
            "id_pays": "ID pays",

            "affiliation_group": {
                "title": "Groupe",
                "func": get_affiliation_group
            }
        }

    },
    "esd": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.esd_service",
        "func_name": "get_all_esds",
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Radiée"
            },
            "type": PM_TYPE_MAPPING,
            "creation_status": CREATION_STATUS_MAPPING,
        },
        "columns": {
            "id": "ID",
            "groupe": "Groupe",
            "motif": "Motif",
            "poc_total": "PC total",
            "poc_actif": "PC actifs",
            "poc_inactif": "PC inactifs",
            "creation_status": "Statut de création",
            "part_total": "Part Total",
            "sequence_number": "Sequence Number",
            "affiliation_group_id": "Affiliation Group ID",
            "affiliation_group_motif": "Groupe Motif",
            "numero_decision_autorisation": "Numero Decision Autorisation",
            "date_decision_autorisation": "Date Decision Autorisation",

            "nature_pm": "Nature PM",
            "numero_autorisation": "Numero autorisation",
            "localite": "Localite",
            "localite_code": "Localite code",
            "region": "Region",
            "centre": "Centre",
            "ville": "Ville",
            "registre_commerce": "RC",
            "adresse": "Adresse",
            "raison_sociale": "RS",
            "idce": "ICE",
            "idf": "IF",
            "forme_juridique": "Forme Juridique",
            "capital_social": "Capital social",
            "statut": "Statut",
            "email": "E-Mail",
            "telephone": "Telephone",
            "date_creation": "Statut de création",
            "date_radiation": "Date de radiation",
            "pays": "Pays",
            "id_pays": "ID pays",

            "affiliation_group": {
                "title": "Groupe",
                "func": get_affiliation_group
            }
        }
    },
    "ep": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.ep_service",
        "func_name": "get_all_eps",
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Radiée"
            },
            "type": PM_TYPE_MAPPING,
            "creation_status": CREATION_STATUS_MAPPING,
        },
        "columns": {
            "id": "ID",
            "groupe": "Groupe",
            "motif": "Motif",
            "poc_total": "PC total",
            "poc_actif": "PC actifs",
            "poc_inactif": "PC inactifs",
            "creation_status": "Statut de création",
            "part_total": "Part Total",
            "sequence_number": "Sequence Number",
            "affiliation_group_id": "Affiliation Group ID",
            "affiliation_group_motif": "Groupe Motif",
            "numero_decision_autorisation": "Numero Decision Autorisation",
            "date_decision_autorisation": "Date Decision Autorisation",

            "nature_pm": "Nature PM",
            "numero_autorisation": "Numero autorisation",
            "localite": "Localite",
            "localite_code": "Localite code",
            "region": "Region",
            "centre": "Centre",
            "ville": "Ville",
            "registre_commerce": "RC",
            "adresse": "Adresse",
            "raison_sociale": "RS",
            "idce": "ICE",
            "idf": "IF",
            "forme_juridique": "Forme Juridique",
            "capital_social": "Capital social",
            "statut": "Statut",
            "email": "E-Mail",
            "telephone": "Telephone",
            "date_creation": "Statut de création",
            "date_radiation": "Date de radiation",
            "pays": "Pays",
            "id_pays": "ID pays",

            "apa_actif": {
                "title": "Agences propres",
                "func": get_apa_actif
            },
            "m_actif": {
                "title": "Mandataires",
                "func": get_m_actif
            },
            "ama_actif": {
                "title": "Agences mandataires",
                "func": get_ama_actif
            },
            "affiliation_group": {
                "title": "Groupe",
                "func": get_affiliation_group
            }
        }
    },
    "mandataire": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.mandataire_service",
        "func_name": "get_all_eps",
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Radiée"
            },
            "creation_status": CREATION_STATUS_MAPPING,
        },
        "columns": {
            "id": "ID",
            "groupe": "Groupe",
            "motif": "Motif",
            "ama_actif": "AMA Actif",
            "amna_actif": "AMNA Actif",
            "creation_status": "Creation Status",
            "sequence_number": "Sequence Number",
            "affiliation_group_id": "Affiliation Group ID",
            "affiliation_group_motif": "Affiliation Group Motif",
            "numero_decision_autorisation": "Numero Decision Autorisation",
            "date_decision_autorisation": "Date Decision Autorisation",

            "nature_pm": "Nature PM",
            "numero_autorisation": "Numero autorisation",
            "localite": "Localite",
            "localite_code": "Localite code",
            "region": "Region",
            "centre": "Centre",
            "ville": "Ville",
            "registre_commerce": "Registre commerce",
            "adresse": "Adresse",
            "raison_sociale": "Raison sociale",
            "idce": "IDCE",
            "idf": "IDF",
            "forme_juridique": "Forme juridique",
            "capital_social": "Capital social",
            "statut": "Statut",
            "email": "Email",
            "telephone": "Telephone",
            "date_creation": "Date de creation",
            "date_radiation": "Date de radiation",
            "pays": "Pays",
            "id_pays": "ID pays"
        }
    },
    "beneficiaire_pm": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION.value, Roles.PREPOSE.value],
        "func_path": "app.main.services.beneficiaire_pm_service",
        "func_name": "get_all_beneficiaire_pms",
        "values_mapping": {
            "statut": {
                1: "Actif",
                2: "Inactif"
            },
            "qualite": QUALITE_BENEFICIAIRE_MAPPING
        },
        "columns": {
            "id": "ID",
            "qualite": "Qualité Client/Bénéficiaire",
            "centre": "Centre",
            "registre_commerce": "Registre commerce",
            "raison_sociale": "Raison sociale",
            "idce": "IDCE",
            "nationalite": "Nationalité",
            "statut": "Statut",

            "poc_id": "POC ID",
            "numero_agrement": "Numero Agrement",
            "nom_agence": "Nom Agence",
            "date_deactivation": "Date Deactivation",
            "type": "Type",
            "date_modification": "Date de modification",
            "modified_by": "Modifié par",
            "motif_modification": "Motif de modification",

        }
    },
    "beneficiaire_pp": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION.value, Roles.PREPOSE.value],
        "func_path": "app.main.services.beneficiaire_pp_service",
        "func_name": "get_all_beneficiaire_pps",
        "values_mapping": {
            "statut": {
                1: "Actif",
                2: "Inactif"
            },
            "qualite": QUALITE_BENEFICIAIRE_MAPPING
        },
        "columns": {
            "id": "ID",
            "prenom": "Prénom",
            "nom": "Nom",
            "qualite": "Qualité Client/Bénéficiaire",
            "nature_piece": "Nature pièce identité",
            "numero_piece": "Numéro pièce d’identité",
            "nationalite": "Nationalité",
            "statut": "Statut",

            "poc_id": "POC ID",
            "numero_agrement": "Numero Agrement",
            "nom_agence": "Nom Agence",
            "date_deactivation": "Date Deactivation",
            "type": "Type",
            "is_final": "Is Final",
            "date_modification": "Date de modification",
            "modified_by": "Modifié par",
            "motif_modification": "Motif de modification",
        }
    },
    "beneficiaire_pc": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER.value, Roles.OC_AGENT.value, Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION.value, Roles.PREPOSE.value],
        "func_path": "app.main.services.beneficiaire_pc_service",
        "func_name": "get_all_beneficiaire_pcs",
        "values_mapping": {
            "qualite": QUALITE_BENEFICIAIRE_MAPPING
        },
        "columns": {
            "id": "ID",
            "qualite": "Qualité Client/Bénéficiaire",
            "numero_agrement": "Numéro agrément",
            "nom_agence": "Dénomination PC",
            "poc_id": "ID Point de change",
        }
    },
    "demande": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.demande_service",
        "func_name": "get_all_demandes",
        "is_multiple_sort": True,
        "values_mapping": {
            "statut": {
                0: "En cours de saisi",
                1: "Traité",
                2: "En cours de validation",
            },
            "qualite": QUALITE_BENEFICIAIRE_MAPPING,
            "decision": {
                1: "Rejetée",
                2: "Acceptée"
            },
            "initiateur": {
                1: "OP",
                2: "OC"
            }
        },
        "columns": {
            "id": "ID",
            "initiateur": "Initiateur",
            "created_by": "Agent Traitant",
            "validateurs": "Validateurs",
            "date_creation": "Date de la demande",
            "motif": "Motif de rejet",
            "denomination_pm": "Dénomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "type_pm": "Type PM",
            "numero_decision_autorisation": "Numéro décision modification",
            "date_decision_autorisation": "Date décision modification",
            "statut": "Avancement",

            "motif": {
                "title": "Motif de modification",
                "func": get_motif,
            },
            "valide_manager_oc": {
                "title": "Etape",
                "func": get_valide_manager_oc
            },
            "decision": "Décision finale",
        }
    },
    "demande_change_modif_view": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.modification_history_service",
        "func_name": "get_all_history_info",
        "values_mapping": {
            "modification_category_op": {
                1: "Scd",
                2: "Esd",
                3: "Ep",
                4: "Mandataire",
                5: "Point de change",
            }
        },
        "columns": {
            "demande_date_creation": "Date modification",
            "modification_motif": "Motif",
            "change_key": "Attribut",
            "change_oldvalue": "Ancienne valeur",
            "change_value": "Nouvelle valeur",  # Valeur attribut
            "demande_initiateur": "Modifié par",

            "id": "ID",
            "demande_id": "Demande ID",
            "demande_scd": "Demande SCD",
            "demande_ep": "Demande EP",
            "demande_esd": "Demande ESD",
            "demande_mandataire_id": "Demande Mandataire ID",
            "demande_status": "Demande Status",
            "demande_poc_id": "Demande POC ID",
            "modification_category_op": "Modification Category Op",
            "change_ecran": "Change Ecran",
        }
    },
    "declaration_poc": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.declaration_service",
        "func_name": "get_all_poc_declarations",
        "is_multiple_sort": True,
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Terminée"
            },
            "decision": {
                1: "Rejetée",
                2: "Validée"
            }
        },
        "columns": {
            "id": "ID",
            "poc_addresse": "POC Adresse",
            "numero_agrement": {
                "title": "№ Agrément",
                "func": get_numero_agrement
            },
            "motif": "Motif",
            "date_debut": "Date début",
            "created_by": "Crée par",
            "validator": "Validator",
            "denomination_pm": "Dénomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "denomination_mandataire": "Dénomination Mandataire",
            "centre_m": "Centre Mandataire",
            "rc_m": "RC Mandataire",
            "statut": "Statut",
            "decision": "Décision",

            "poc_id": "POC ID",
            "nom_agence": "Nom Agence",
            "type_pm": "Type PM",
            "date_demande": "Date Demande",
            "date_fin": "Date Fin",
            "date_declaration_m": "Date Declaration M",
        }
    },
    "declaration_pm": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_MANAGER, Roles.OC_AGENT],
        "func_path": "app.main.services.declaration_service",
        "func_name": "get_all_pm_declarations",
        "is_multiple_sort": True,
        "values_mapping": {
            "statut": {
                0: "En cours de saisie",
                1: "Traité",
                2: "En cours de validation"
            },
            "decision": {
                1: "Rejetée",
                2: "Acceptée"
            },
            "type_pm": PM_TYPE_MAPPING
        },
        "columns": {
            "id": "ID",
            "pm_id": {
                "title": "Identifiant PM",
                "func": get_pm_id
            },
            "centre_pm": "Centre",
            "rc_pm": "RC",
            "denomination_pm": "Raison sociale",
            "type_pm": "Type",
            "created_by": "Agent",
            "validator": "Validateur",
            "date_demande": "Date de la demande",
            "statut": "Avancement",
            "decision": "Décision finale"
        }
    },
    "declaration_fiscal": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.declaration_service",
        "func_name": "get_all_fiscal_declarations",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "created_by": "Crée par",
            "denomination_pm": "Dénomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "date_declaration": "Date déclaration",
            "annee_comptable_de": "Année déclaration",

            "date_debut": "Date Debut",
            "date_fin": "Date Fin",
            "capital_social": "Capital Social",
            "capitaux_propres": "Capitaux Propres",
            "chiffre_affaires": "Chiffre Affaires",
            "resultat_exploitation": "Resultat Exploitation",
            "resultat_net": "Resultat Net",
            "resultat_fiscal": "Resultat Fiscal",
            "resultat_financier": "Resultat Financier",
            "charges_personnel": "Charges Personnel",
            "charges_exploitation": "Charges Exploitation",
            "produits_financiers": "Produits Financiers",
            "documents": "Documents",
            "scd_id": "SCD ID",
        }
    },
    "declaration_liasse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.declaration_service",
        "func_name": "get_all_fiscal_declarations",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "created_by": "Crée par",
            "denomination_pm": "Dénomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "date_declaration": "Date déclaration",
            "annee_comptable_de": "Année déclaration",

            "date_debut": "Date Debut",
            "date_fin": "Date Fin",
            "capital_social": "Capital Social",
            "capitaux_propres": "Capitaux Propres",
            "chiffre_affaires": "Chiffre Affaires",
            "resultat_exploitation": "Resultat Exploitation",
            "resultat_net": "Resultat Net",
            "resultat_fiscal": "Resultat Fiscal",
            "resultat_financier": "Resultat Financier",
            "charges_personnel": "Charges Personnel",
            "charges_exploitation": "Charges Exploitation",
            "produits_financiers": "Produits Financiers",
            "documents": "Documents",
            "scd_id": "SCD ID",
        }
    },
    "declaration_docs": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "declaration_fiscal_id": "Declaration Fiscal ID",
            "intitule_document": "Intitule Document",
            "nom_fichier": "Nom Fichier",
            "date_creation": "Date Creation",
            "full_path": "Full Path",
            "file_extension": "File Extension"
        }
    },
    "user": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "role": ROLES_MAPPING,
        },
        "columns": {
            "id": "ID",
            "fullname": "Nom complet",
            "email": "Adresse e-mail",
            "role": "Rôle",
            "created_on": "Créé le",
            "modified_on": "Modifié le",

            "keycloak_id": "Keycloak ID",
            "firstName": "First Name",
            "lastName": "Last Name",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "poc_id": "POC ID",
        }
    },
    "modification": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.modification_service",
        "func_name": "get_all_modification_info",
        "values_mapping": {
            "motif_status": {
                True: "Actif",
                False: "Inactif"
            },
            "op_category": {
                1: "Scd",
                2: "Esd",
                3: "Ep",
                4: "Mandataire",
                5: "Point de change",
            },
            "pattern": {
                1: "Modifier par OP sans validation",
                2: "Modifier par OP avec validation",
                3: "Modifier par OC"
            }
        },
        "columns": {
            "id": "ID",
            "motif": "Motif",
            "motif_status": "Statut",
            "date_activation": "Date d'activation",
            "date_desactivation": "Date de désactivation",
            "pattern": {
                "title": "Pattern",
                "func": get_pattern
            },

            "modifications": "Modifications",
            "op_category": "Operation Category",
            "is_add": "Is Add",
            "date_modification": "Date Modification",
        }
    },
    "affiliation_group": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.affiliation_group_service",
        "func_name": "get_all_affiliation_groups",
        "values_mapping": {
            "type_operator": {
                1: "Scd",
                2: "Esd",
                3: "Ep",
                4: "Mandataire",
            }
        },
        "columns": {
            "id": "ID",
            "name": "Nom",
            "description": "Description",
            "type_operator": "Catégorie Opérateur"
        }
    },
    "lieu_implantation": {
        "required_roles": [Roles.OC_ADMIN.value, Roles.OC_SUPER_ADMIN.value, Roles.OC_AGENT.value, Roles.OP.value, Roles.OC_MANAGER.value],
        "func_path": "app.main.services.lieu_implantation_service",
        "func_name": "get_all_lieu_implantations",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "label": "Lieu d’implantation",
            "creation_date": "Date création",
            "modification_date": "Date modification"
        }
    },
    "sous_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value, Roles.OC_AGENT.value, Roles.OC_MANAGER.value, Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION.value],
        "func_path": "app.main.services.sub_operation_service",
        "func_name": "get_all_sub_operations",
        "values_mapping": {
            "type_operation": Type_Operation_MAPPING,
            "statut": {
                True: "Actif",
                False: "Inactif"
            }
        },
        "columns": {
            "id": "ID",
            "code": "Code Sous-opération",
            "type_operation": "Opération",
            "code_statistique": "Code statistique Sous-opération",
            "label": "Sous-opération",
            "statut": "Statut",
            "nature_beneficiaire": "Qualité bénficiaire",
            "beneficiaire_final_required": "Bénéficiaire = bénéficiaire final",
            "nature_beneficiaire_final": "Qualité bénficiaire final",
            "date_activation": "Date d’activation",
            "date_desactivation": "Date désactivation",

            "attachements": "Attachements",
            "cancel_deadline_id": "Cancel Deadline ID"
        }
    },
    "authorized_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.authorized_operation_service",
        "func_name": "get_all_authorized_operations",
        "values_mapping": {
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "type_operation": Type_Operation_MAPPING,
            "statut": {
                True: "Actif",
                False: "Inactif"
            }
        },
        "columns": {
            "id": "ID",
            "sous_operation_code": {
                "title": "Code sous-opération",
                "func": get_sous_operation_code
            },
            "type_operation": "Opération",
            "sous_operation_code_statistique": {
                "title": "Code statistique Sous-opération",
                "func": get_sous_operation_code_statistique
            },
            "sous_operation_label": {
                "title": "Sous Opération",
                "func": get_sous_operation_label
            },
            "categorie_pc": "Catégorie du point de change",
            "lieu_implantations": {
                "title": "Lieu d’implantation",
                "func": get_sous_operation_lieu_implantations,
            },
            "support_mad": {
                "title": "Support MAD",
                "func": get_payment_method
            },
            "support_devise": {
                "title": "Support DEVISE",
                "func": get_payment_method
            },
            "statut": "Statut",
            "date_activation": "Date d’activation",
            "date_desactivation": "Date de désactivation",

            "lieu_implantations_hash": "Lieu Implantations Hash",
            "sous_operation_id": "Sous Operation ID"
        }
    },
    "derogation_encaisse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_AGENT.value, Roles.OC_MANAGER.value],
        "func_path": "app.main.services.derogation_encaisse_service",
        "func_name": "get_all_derogation_encaisses",
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Validée"
            }
        },
        "columns": {
            "operator_pm": {
                "title": "Opérateur PM",
                "func": get_operator_pm
            },
            "encaisse": "Encaisse",
            "numero_decision": "Numéro de la décision",
            "date_decision": "Date de la décision",
            "created_by": "Créé par",
            "statut": "Statut",
            "validated_by": "Validé par",

            "id": "ID",
            "type": "Type",
            "scd_id": "SCD ID",
        }
    },
    "derogation_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_AGENT.value, Roles.OC_MANAGER.value],
        "func_path": "app.main.services.derogation_operation_service",
        "func_name": "get_all_derogation_operations",
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Validée"
            },
            "categorie_pc": {
                1: "Point de change SCD",
                2: "Agence Propre Agrée",
                3: "Agence Propre Non Agrée",
                4: "Agence Mandataire Agrée",
                5: "Agence Mandataire Non Agrée",
                6: "Esd",
                7: "Banque"
            },
            "is_included": {
                True: "Inclure",
                False: "Exclure"
            }
        },
        "columns": {
            "derogation_op": {
                "title": "Opérateur PM",
                "func": get_derogration_op
            },
            "authorized_operation_id": "Opération ID",
            "is_included": "Inclure/Exclure",
            "numero_decision": "Numéro de la décision",
            "date_decision": "Date de la décision",
            "created_by": "Créé par",
            "statut": "Statut",
            "validated_by": "Validé par",

            "id": "ID",
            "type": "Type",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "mandataire_id": "Mandataire ID",
            "categorie_pc": "Categorie PC",
        }
    },
    "seuil_encaisse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value],
        "func_path": "app.main.services.seuil_encaisse_service",
        "func_name": "get_all_seuil_encaisses",
        "values_mapping": {
            "categorie_pc": CATEGORIE_PC_MAPPING,
        },
        "columns": {
            "id": "ID",
            "annee": "Année",
            "categorie_pc": "Catégorie du Point de change",
            "lieu_implantation": {
                "title": "Lieu d’implantation",
                "func": get_lieu_implantation_label
            },
            "encaisse": "Encaisse",
            "latence_jours": {
                "title": "Temps de latence",
                "func": get_latence_jours
            },

            "latence_heure": "Latence Heure",
        }
    },
    "cancel_deadline": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value],
        "func_path": "app.main.services.cancel_deadline_service",
        "func_name": "get_all_cancel_deadlines",
        "values_mapping": {
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "type_operation": Type_Operation_MAPPING,
        },
        "columns": {
            "id": "ID",
            "categorie_pc": "Catégorie du Point de change",
            "type_operation": "Opération",
            "delai": {
                "title": "Délai d’annulation",
                "func": get_delai
            }
        }
    },
    "plafond_dotation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value],
        "func_path": "app.main.services.plafond_dotation_service",
        "func_name": "get_all_plafond_dotations",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "annee": "Année",
            "sous_operation_id": {
                "title": "Sous-opération",
                "func": get_sous_operation_label
            },
            "plafond": "Plafond de dotation",
        }
    },
    "complement_dotation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value],
        "func_path": "app.main.services.complement_dotation_service",
        "func_name": "get_all_complement_dotations",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "annee": "Année",
            "label": "Libellé du complément",
            "sous_operation_code": {
                "title": "ID sous-opération",
                "func": get_sous_operation_code
            },
            "sous_operation_label": {
                "title": "Sous-opération",
                "func": get_sous_operation_label
            },
            "nature_beneficiaire": {
                "title": "Bénéficiaire",
                "func": get_nature_beneficiaire
            },
            "base_calcul": "Base de calcul",
            "percentage": "%",
            "plafond": "Plafond de la dotation",

            "sous_operation_id": "Sous Operation ID"
        }
    },
    "caisse_devise": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OP.value, Roles.PREPOSE.value],
        "func_path": "app.main.services.caisse_devise_service",
        "func_name": "consult_caisse",
        "values_mapping": {
            "categorie_pc": CATEGORIE_PC_MAPPING,
        },
        "columns": {
            "id": "ID",
            "nom_agence": "Dénomination PC",
            "categorie_pm": "Catégorie PM",
            "raison_sociale_pm": "RS (PM)",
            "registre_commerce": "RC",
            "centre": "Centre",
            "categorie_pc": "Catégorie PC",
            "numero_agrement": "N°Agrément",

            # Columns for Prepose
            "label": "Codes",
            "montant": "Montant de la caisse de tout le point de change"
        }
    },
    "encaisse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value, Roles.OP.value, Roles.PREPOSE.value],
        "func_path": "app.main.services.encaisse_service",
        "func_name": "consult_encaisse",
        "values_mapping": {
            "categorie_pc": CATEGORIE_PC_MAPPING,
        },
        "columns": {
            "id": "ID",
            "categorie_pm": "Catégorie Opérateur (PM)",
            "raison_sociale_pm": "RS",
            "registre_commerce": "RC",
            "centre": "Centre",
            "categorie_pc": "Catégorie PC",
            "nom_agence": "Point de change dénomination",
            "numero_agrement": "N°Agrément",

            # Columns for Prepose
            "encaisse": "Montant de l’encaisse en MAD (*)",
        }
    },
    "individual": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.cnasnu_service",
        "func_name": "get_international_individuals",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "full_name": "Nom complet",
            "low_aliases": "Good aliases",
            "good_aliases": "Good aliases",
            "identity_documents": "ID documents",
            "date_creation": {
                "title": "Date de création",
                "func": get_only_date
            },
        }
    },
    "local_individual": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.cnasnu_service",
        "func_name": "get_local_individuals",
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "first_name": "Nom",
            "last_name": "Prénom",
            "date_creation": {
                "title": "Date de création",
                "func": get_only_date
            },
            "cin": {
                "title": "CIN",
                "func": get_cin,
            },
            "passport": {
                "title": "Passport",
                "func": get_passport,
            },
        }
    },
    "autorisation_particuliere_pm": {
        "required_roles": [Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION],
        "func_path": "app.main.services.autorisation_particuliere_pm_service",
        "func_name": "get_all_autorisation_particuliere_pms",
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Validé",
                3: "Rejeté",
            }
        },
        "columns": {
            "sous_operation": {
                "title": "Type de sous-opération",
                "func": get_sous_operation_label
            },
            "beneficiaire_qualite": {
                "title": "Qualité du bénéficiaire",
                "func": get_beneficiaire_pm_qualite
            },
            "registre_commerce": {
                "title": "RC",
                "func": get_beneficiaire_pm_field_value
            },
            "centre": {
                "title": "Centre",
                "func": get_beneficiaire_pm_field_value
            },
            "raison_sociale": {
                "title": "Raison Sociale",
                "func": get_beneficiaire_pm_field_value
            },
            "montant_supplementaire": "Montant supplémentaire accordé",
            "numero_autorisation": "Numéro d’autorisation",
            "date_autorisation": "Date d’autorisation",
            "date_debut_effet": "Date début effet",
            "date_fin_effet": "Date fin effet",
            "statut": "Statut",
            "created_by": "Créé par",
            "date_creation": "Date création",
            "validated_by": "Validée par",
            "date_validation": "Date validation",
            "commentaire": "Commentaire",
        }
    },
    "autorisation_particuliere_pp": {
        "required_roles": [Roles.AGENT_AUTORISATION.value, Roles.MANAGER_AUTORISATION],
        "func_path": "app.main.services.autorisation_particuliere_pp_service",
        "func_name": "get_all_autorisation_particuliere_pps",
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Validé",
                3: "Rejeté",
            },
            "flag_desactivation_complement_dotation": {
                True: "Oui",
                False: "Non"
            }
        },
        "columns": {
            "sous_operation": {
                "title": "Type de sous-opération",
                "func": get_sous_operation_label
            },
            "beneficiaire_qualite": {
                "title": "Qualité du bénéficiaire",
                "func": get_beneficiaire_pp_qualite
            },

            "nom": {
                "title": "Nom",
                "func": get_beneficiaire_pp_field_value
            },
            "prenom": {
                "title": "Prénom",
                "func": get_beneficiaire_pp_field_value
            },
            "nature_piece": {
                "title": "Nature de la pièce d’identité",
                "func": get_beneficiaire_pp_field_value
            },
            "numero_piece": {
                "title": "Numéro de la pièce d’identité",
                "func": get_beneficiaire_pp_field_value
            },
            "nationalite": {
                "title": "Nationalité",
                "func": get_beneficiaire_pp_field_value
            },
            "montant_supplementaire": "Montant supplémentaire accordé",
            "numero_autorisation": "Numéro d’autorisation",
            "date_autorisation": "Date d’autorisation",
            "annee_effet": "Année effet autorisation",
            "flag_desactivation_complement_dotation": "Flag désactivation complément de dotation",
            "statut": "Statut",
            "created_by": "Créé par",
            "date_creation": "Date création",
            "validated_by": "Validée par",
            "date_validation": "Date de validation",
            "commentaire": "Commentaire",
        }
    }
}
