from oc_lib.utils.constants import Roles


EXPORT_TABLE_INFO = {
    "operation_achat_view": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            }
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",
            "numero_bordereau": "Numero de bordereau",
            "date_bordereau": "Date de bordereau",
            "categorie_op": "Categorie op",
            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "categorie_pc": "Categorie pc",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "poc_adresse": "Poc adresse",
            "created_by": "Created by",
            "date_creation": "Date de creation",
            "beneficiaire_pm_qualite": "Beneficiaire pm qualite",
            "beneficiaire_pp_qualite": "Beneficiaire pp qualite",
            "sous_operation_label": "Sous operation label",
            "sous_operation_id": "Sous operation ID",
            "beneficiaire_pp_id": "Beneficiaire pp ID",
            "beneficiaire_pp_nature_piece": "Beneficiaire pp nature piece",
            "beneficiaire_pp_numero_piece": "Beneficiaire pp numero piece",
            "beneficiaire_pp_nom": "Beneficiaire pp nom",
            "beneficiaire_pp_prenom": "Beneficiaire pp prenom",
            "beneficiaire_pp_nationalite": "Beneficiaire pp nationalite",
            "beneficiaire_pm_id": "Beneficiaire pm ID",
            "beneficiaire_pm_registre_commerce": "Beneficiaire pm registre commerce",
            "beneficiaire_pm_centre": "Beneficiaire pm centre",
            "beneficiaire_pm_raison_sociale": "Beneficiaire pm raison sociale",
            "beneficiaire_pm_idce": "Beneficiaire pm IDCE",
            "numero_declaration": "Numero de declaration",
            "date_declaration": "Date de declaration",
            "statut": "Statut",
            "devise_labels": "Devise labels",
            "montant_global": "Montant global",
            "support_mad": "Support MAD"
        }
    },
    "operation_vente_view": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            }
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",
            "numero_bordereau": "Numero de bordereau",
            "date_bordereau": "Date de bordereau",
            "categorie_op": "Categorie op",
            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "categorie_pc": "Categorie pc",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "poc_adresse": "Poc adresse",
            "created_by": "Created by",
            "date_creation": "Date de creation",
            "beneficiaire_pm_qualite": "Beneficiaire pm qualite",
            "beneficiaire_pp_qualite": "Beneficiaire pp qualite",
            "beneficiaire_final_pp_qualite": "Beneficiaire final pp qualite",
            "sous_operation_label": "Sous operation label",
            "sous_operation_id": "Sous operation ID",
            "beneficiaire_pp_id": "Beneficiaire pp ID",
            "beneficiaire_pp_nature_piece": "Beneficiaire pp nature piece",
            "beneficiaire_pp_numero_piece": "Beneficiaire pp numero piece",
            "beneficiaire_pp_nom": "Beneficiaire pp nom",
            "beneficiaire_pp_prenom": "Beneficiaire pp prenom",
            "beneficiaire_pp_nationalite": "Beneficiaire pp nationalite",
            "beneficiaire_final_pp_nature_piece": "Beneficiaire final pp nature piece",
            "beneficiaire_final_pp_numero_piece": "Beneficiaire final pp numero piece",
            "beneficiaire_final_pp_nom": "Beneficiaire final pp nom",
            "beneficiaire_final_pp_prenom": "Beneficiaire final pp prenom",
            "beneficiaire_pm_id": "Beneficiaire pm ID",
            "beneficiaire_pm_registre_commerce": "Beneficiaire pm registre commerce",
            "beneficiaire_pm_centre": "Beneficiaire pm centre",
            "beneficiaire_pm_raison_sociale": "Beneficiaire pm raison sociale",
            "beneficiaire_pm_idce": "Beneficiaire pm IDCE",
            "numero_autorisation": "Numero autorisation",
            "statut": "Statut",
            "devise_labels": "Devise labels",
            "montant_global": "Montant global",
            "support_mad": "Support MAD"
        }
    },
    "operation_cession_view": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Enregistrée",
                2: "Annulée"
            }
        },
        "columns": {
            "id": "ID",
            "op_id": "Operation ID",
            "numero_bordereau": "Numero de bordereau",
            "date_cession": "Date de cession",
            "categorie_op": "Categorie op",
            "pm_raison_sociale": "Pm raison sociale",
            "pm_registre_commerce": "Pm registre commerce",
            "pm_centre": "Pm centre",
            "categorie_pc": "Categorie pc",
            "poc_id": "Poc ID",
            "poc_denomination": "Poc denomination",
            "poc_numero_agrement": "Poc numero agrement",
            "created_by": "Created by",
            "date_creation": "Date de creation",
            "code_banque": "Code banque",
            "code_agence": "Code agence",
            "devise_labels": "Devise labels",
            "montant_global": "Montant global",
            "total_devises": "Total devises",
            "statut": "Statut"
        }
    },
    "poc": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "creation_status": {
                0: "En cours",
                1: "Validated",
                2: "En attente de validation"
            },
            "statut_activite": {
                1: "EN ACTIVITE",
                2: "ARRET PROVISOIRE",
                3: "SUSPENSION_FERME",
                4: "SUSPENSION_OUVERTE",
                5: "RETIRE",
                6: "ANNULE",
                7: "EN_ARRET",
            },
            "statut_agrement": {
                1: "ACTIF",
                2: "INACTIF",
                3: "NEANT"
            },
            "categorie": {
                1: "Point de change SCD",
                2: "Agence Propre Agrée",
                3: "Agence Propre Non Agrée",
                4: "Agence Mandataire Agrée",
                5: "Agence Mandataire Non Agrée",
                6: "Esd",
                7: "Banque"
            }
        },
        "columns": {
            "id": "ID",
            "forme_juridique": "Forme Juridique",
            "is_link": "Is Link",
            "is_source": "Is Source",
            "motif": "Motif",
            "secteur_activite": "Secteur Activite",
            "nature": "Nature",
            "nom_agence": "Nom Agence",
            "adresse": "Adresse",
            "date_modification_adresse": "Date Modification Adresse",
            "localite": "Localite",
            "localite_code": "Localite Code",
            "region": "Region",
            "is_agrement": "Is Agrement",
            "is_permanent": "Is Permanent",
            "numero_agrement": "Numero Agrement",
            "encaisse": "Encaisse",
            "seuil_encaisse": "Seuil Encaisse",
            "seuil_encaisse_depasse": "Seuil Encaisse Depasse",
            "flag_retablissement_agrement": "Flag Retablissement Agrement",
            "date_retablissement_agrement": "Date Retablissement Agrement",
            "date_modification_encaisse": "Date Modification Encaisse",
            "date_debut_activite": "Date Debut Activite",
            "date_fin_activite": "Date Fin Activite",
            "statut_activite": "Statut Activite",
            "statut_agrement": "Statut Agrement",
            "raison_sociale_pm": "Raison Sociale PM",
            "creation_status": "Creation Status",
            "categorie": "Categorie",
            "scd_id": "SCD ID",
            "esd_id": "ESD ID",
            "ep_id": "EP ID",
            "mandataire_id": "Mandataire ID",
            "lieu_implantation_id": "Lieu Implantation ID",
            "linked_poc_id": "Linked POC ID"
        }
    },
    "pp": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                True: "Active",
                False: "Inactive"
            },
        },
        "columns": {
            "id": "ID",
            "nom": "Nom",
            "prenom": "Prenom",
            "nature_piece": "Nature Piece",
            "numero_piece": "Numero Piece",
            "nationalite": "Nationalite",
            "adresse": "Adresse",
            "email": "Email",
            "phone": "Phone",
            "nature_pp": "Nature PP",
            "date_nomination": "Date Nomination",
            "date_demission": "Date Demission",
            "statut": "Statut",
        }
    },
    "pm": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Active",
                2: "Inactive"
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
            "id_pays": "ID pays",
            "type": "Type"
        }
    },
    "scd": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "poc_total": "Poc Total",
            "poc_actif": "Poc Actif",
            "poc_inactif": "Poc Inactif",
            "creation_status": "Creation Status",
            "part_total": "Part Total",
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
    "esd": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "part_total": "Part Total",
            "creation_status": "Creation Status",
            "sequence_number": "Sequence Number",
            "groupe": "Groupe",
            "motif": "Motif",
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
    "ep": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
            "apa_actif": "APA Actif",
            "apna_actif": "APNA Actif",
            "m_actif": "M Actif",
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
    "mandataire": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
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
        "values_mapping": {
            "statut": {
                1: "ACTIF",
                2: "INACTIF"
            }
        },
        "columns": {
            "id": "ID",
            "qualite": "Qualite",
            "nationalite": "Nationalite",
            "poc_id": "POC ID",
            "numero_agrement": "Numero Agrement",
            "nom_agence": "Nom Agence",
            "date_deactivation": "Date Deactivation",
            "statut": "Statut",
            "type": "Type",
            "registre_commerce": "Registre Commerce",
            "centre": "Centre",
            "raison_sociale": "Raison Sociale",
            "idce": "IDCE"
        }
    },
    "beneficiaire_pp": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Saved",
                2: "Cancelled"
            }
        },
        "columns": {
            "id": "ID",
            "qualite": "Qualite",
            "nationalite": "Nationalite",
            "poc_id": "POC ID",
            "numero_agrement": "Numero Agrement",
            "nom_agence": "Nom Agence",
            "date_deactivation": "Date Deactivation",
            "statut": "Statut",
            "type": "Type",
            "nom": "Nom",
            "prenom": "Prenom",
            "nature_piece": "Nature Piece",
            "numero_piece": "Numero Piece",
            "is_final": "Is Final"
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
