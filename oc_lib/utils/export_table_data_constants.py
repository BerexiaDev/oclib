from oc_lib.utils.constants import Roles
from oc_lib.utils.export_table_data_func import get_designation_agence, get_poc_id, get_pp_field_name, \
    get_lieu_implantation_label, get_categorie_op, get_pm_id, get_affiliation_group, get_apa_actif, \
    get_m_actif, get_ama_actif, get_pm, get_poc, get_motif, get_valide_manager_oc

CATEGORIE_PC_MAPPING = {
    1: "Société de change de devises",
    2: "Etablissement de paiement – Agences propres agréée",
    3: "Etablissement de paiement – Agences propres non-agréée",
    4: "Etablissement de paiement – Agences Mandataires agréée",
    5: "Etablissement de paiement – Agences Mandataires non-agréée",
    6: "Etablissement Sous Délégataire",
    7: "Banque"
}

QUALITE_BENEFICIAIRE_MAPPING = {
    1: "PM-Résident",
    2: "PM-Non Résident",
    3: "PP-Etranger non Résident",
    4: "PP-Etranger Résident",
    5: "PP-Marocain Résident",
    6: "PP-Marocain non résident (MRE)",
    7: "Point de change",
}

EXPORT_TABLE_INFO = {
    "operation_achat_view": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.operation_achat_service",
        "func_name": "get_all_operation_achats",
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            },
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
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.operation_vente_service",
        "func_name": "get_all_operation_ventes",
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            },
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
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "func_path": "app.main.services.operation_cession_service",
        "func_name": "get_all_operation_cessions",
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            },
            "categorie_pc": CATEGORIE_PC_MAPPING,
            "is_late": {
                True: "Oui",
                False: "Non"
            }
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
            "creation_status": {
                0: "En cours de saisi",
                1: "Validé",
                2: "En cours de validation",
                3: "En cours de demande modification",
                4: "Rejeté"
            },
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
            "is_agrement": {
                True: "Oui",
                False: "Non"
            },
            "is_permanent": {
                True: "Oui",
                False: "Non"
            },
            "is_link": {
                True: "Oui",
                False: "Non"
            }
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
            # "numero_delivrance": {
            #     "title": "N° délivrance décision premier agrément"
            # },
            # "date_delivrance": {
            #     "title": "Date délivrance décision premier agrément"
            # },
            "lieu_implantation": {
                "title": "Lieu Implantation",
                "func": get_lieu_implantation_label
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
            "type": {
                "associe_pm": "Associé",
                "ep": "Ep",
                "esd": "Esd",
                "gerantpm": "Gérant",
                "mandataire": "Mandataire",
                "scd": "Scd"
            },
            "creation_status": {
                0: "En cours de saisi",
                1: "Validé",
                2: "En cours de validation",
                3: "En cours de demande modification",
                4: "Rejeté"
            },
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
            "type": {
                "associe_pm": "Associé",
                "ep": "Ep",
                "esd": "Esd",
                "gerantpm": "Gérant",
                "mandataire": "Mandataire",
                "scd": "Scd"
            },
            "creation_status": {
                0: "En cours de saisi",
                1: "Validé",
                2: "En cours de validation",
                3: "En cours de demande modification",
                4: "Rejeté"
            },
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
            "type": {
                "associe_pm": "Associé",
                "ep": "Ep",
                "esd": "Esd",
                "gerantpm": "Gérant",
                "mandataire": "Mandataire",
                "scd": "Scd"
            },
            "creation_status": {
                0: "En cours de saisi",
                1: "Validé",
                2: "En cours de validation",
                3: "En cours de demande modification",
                4: "Rejeté"
            },
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
            "type": {
                "associe_pm": "Associé",
                "ep": "Ep",
                "esd": "Esd",
                "gerantpm": "Gérant",
                "mandataire": "Mandataire",
                "scd": "Scd"
            },
            "creation_status": {
                0: "En cours de saisi",
                1: "Validé",
                2: "En cours de validation",
                3: "En cours de demande modification",
                4: "Rejeté"
            },
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
                2: "Inactive"
            },
            "creation_status": {
                1: "Created",
                2: "Cancelled"
            },
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
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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

        }
    },
    "beneficiaire_pp": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "is_final": "Is Final"
        }
    },
    "beneficiaire_pc": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "motif_oc_manager_decision": "Motif de rejet",
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
            "id": "ID",
            "demande_id": "Demande ID",
            "demande_initiateur": "Demande Initiateur",
            "demande_date_creation": "Demande Date Creation",
            "demande_scd": "Demande SCD",
            "demande_ep": "Demande EP",
            "demande_esd": "Demande ESD",
            "demande_mandataire_id": "Demande Mandataire ID",
            "demande_status": "Demande Status",
            "demande_poc_id": "Demande POC ID",
            "modification_category_op": "Modification Category Op",
            "modification_motif": "Modification Motif",
            "change_ecran": "Change Ecran",
            "change_key": "Change Key",
            "change_value": "Change Value",
            "change_oldvalue": "Change Oldvalue",
        }
    },
    "declaration_poc": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Inactive"
            },
            "decision": {
                1: "Approved",
                2: "Rejected"
            }
        },
        "columns": {
            "id": "ID",
            "poc_id": "POC ID",
            "poc_addresse": "POC Address",
            "numero_agrement": "Numero Agrement",
            "nom_agence": "Nom Agence",
            "type_pm": "Type PM",
            "date_demande": "Date Demande",
            "motif": "Motif",
            "created_by": "Created By",
            "validator": "Validator",
            "date_debut": "Date Debut",
            "date_fin": "Date Fin",
            "denomination_pm": "Denomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "denomination_mandataire": "Denomination Mandataire",
            "centre_m": "Centre M",
            "rc_m": "RC M",
            "date_declaration_m": "Date Declaration M",
            "statut": "Statut",
            "decision": "Decision"
        }
    },
    "declaration_pm": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Inactive"
            },
            "decision": {
                1: "Accepté",
                2: "Rejetée"
            }
        },
        "columns": {
            "id": "ID",
            "type_pm": "Type PM",
            "denomination_pm": "Denomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "centre_m": "Centre M",
            "rc_m": "RC M",
            "created_by": "Created By",
            "validator": "Validator",
            "date_demande": "Date Demande",
            "statut": "Statut",
            "decision": "Decision",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "mandataire_id": "Mandataire ID"
        }
    },
    "declaration_fiscal": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "created_by": "Created By",
            "denomination_pm": "Denomination PM",
            "centre_pm": "Centre PM",
            "rc_pm": "RC PM",
            "date_declaration": "Date Declaration",
            "annee_comptable_de": "Annee Comptable De",
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
        },
        "columns": {
            "id": "ID",
            "keycloak_id": "Keycloak ID",
            "firstName": "First Name",
            "lastName": "Last Name",
            "fullname": "Full Name",
            "email": "Email",
            "role": "Role",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "poc_id": "POC ID",
            "created_on": "Created On",
            "modified_on": "Modified On"
        }
    },
    "modification": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "motif_status": {
                True: "ACTIF",
                False: "INACTIF"
            },
            "op_category": {
                1: "Scd",
                2: "Esd",
                3: "Ep",
                4: "Mandataire",
                5: "Point de change",
            }
        },
        "columns": {
            "id": "ID",
            "motif": "Motif",
            "modifications": "Modifications",
            "op_category": "Operation Category",
            "motif_status": "Motif Status",
            "is_add": "Is Add",
            "date_activation": "Date Activation",
            "date_modification": "Date Modification",
            "date_desactivation": "Date Desactivation",
            "pattern_id": "Pattern ID"
        }
    },
    "affiliation_group": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "name": "Name",
            "description": "Description",
            "type_operator": "Type Operator"
        }
    },
    "lieu_implantation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "label": "Label",
            "creation_date": "Creation Date",
            "modification_date": "Modification Date"
        }
    },
    "sous_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "type_operation": {
                1: "Achat",
                2: "Vente",
                3: "Cession"
            },
            "statut": {
                True: "ACTIF",
                False: "INACTIF"
            }
        },
        "columns": {
            "id": "ID",
            "type_operation": "Type Operation",
            "code": "Code",
            "code_statistique": "Code Statistique",
            "label": "Label",
            "statut": "Statut",
            "date_activation": "Date Activation",
            "date_desactivation": "Date Desactivation",
            "nature_beneficiaire": "Nature Beneficiaire",
            "nature_beneficiaire_final": "Nature Beneficiaire Final",
            "beneficiaire_final_required": "Beneficiaire Final Required",
            "attachements": "Attachements",
            "cancel_deadline_id": "Cancel Deadline ID"
        }
    },
    "authorized_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "categorie_pc": {
                1: "Point de change SCD",
                2: "Agence Propre Agrée",
                3: "Agence Propre Non Agrée",
                4: "Agence Mandataire Agrée",
                5: "Agence Mandataire Non Agrée",
                6: "Esd",
                7: "Banque"
            },
            "type_operation": {
                1: "Achat",
                2: "Vente",
                3: "Cession"
            },
            "statut": {
                True: "ACTIF",
                False: "INACTIF"
            }
        },
        "columns": {
            "id": "ID",
            "categorie_pc": "Categorie PC",
            "type_operation": "Type Operation",
            "support_mad": "Support MAD",
            "support_devise": "Support Devise",
            "statut": "Statut",
            "date_activation": "Date Activation",
            "date_desactivation": "Date Desactivation",
            "lieu_implantations_hash": "Lieu Implantations Hash",
            "sous_operation_id": "Sous Operation ID"
        }
    },
    "derogation_encaisse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "En cours",
                2: "Validée"
            }
        },
        "columns": {
            "id": "ID",
            "type": "Type",
            "numero_decision": "Numero Decision",
            "date_decision": "Date Decision",
            "created_by": "Created By",
            "statut": "Statut",
            "validated_by": "Validated By",
            "scd_id": "SCD ID",
            "encaisse": "Encaisse",
        }
    },
    "derogation_operation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
        },
        "columns": {
            "id": "ID",
            "type": "Type",
            "numero_decision": "Numero Decision",
            "date_decision": "Date Decision",
            "created_by": "Created By",
            "statut": "Statut",
            "validated_by": "Validated By",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "mandataire_id": "Mandataire ID",
            "categorie_pc": "Categorie PC",
            "authorized_operation_id": "Authorized Operation ID",
            "is_included": "Is Included"
        }
    },
    "seuil_encaisse": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "categorie_pc": {
                1: "Point de change SCD",
                2: "Agence Propre Agrée",
                3: "Agence Propre Non Agrée",
                4: "Agence Mandataire Agrée",
                5: "Agence Mandataire Non Agrée",
                6: "Esd",
                7: "Banque"
            },
        },
        "columns": {
            "id": "ID",
            "annee": "Annee",
            "categorie_pc": "Categorie PC",
            "encaisse": "Encaisse",
            "latence_jours": "Latence Jours",
            "latence_heure": "Latence Heure",
            "lieu_implantation_id": "Lieu Implantation ID"
        }
    },
    "cancel_deadline": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "categorie_pc": {
                1: "Point de change SCD",
                2: "Agence Propre Agrée",
                3: "Agence Propre Non Agrée",
                4: "Agence Mandataire Agrée",
                5: "Agence Mandataire Non Agrée",
                6: "Esd",
                7: "Banque"
            },
            "type_operation": {
                1: "Achat",
                2: "Vente",
                3: "Cession"
            }
        },
        "columns": {
            "id": "ID",
            "categorie_pc": "Categorie PC",
            "type_operation": "Type Operation",
            "delai": "Delai"
        }
    },
    "plafond_dotation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "annee": "Annee",
            "plafond": "Plafond",
            "sous_operation_id": "Sous Operation ID"
        }
    },
    "complement_dotation": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
        },
        "columns": {
            "id": "ID",
            "annee": "Annee",
            "label": "Label",
            "nature_beneficiaire": "Nature Beneficiaire",
            "base_calcul": "Base Calcul",
            "percentage": "Percentage",
            "plafond": "Plafond",
            "sous_operation_id": "Sous Operation ID"
        }
    }
}
