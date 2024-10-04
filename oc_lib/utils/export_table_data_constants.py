from oc_lib.utils.constants import Roles


EXPORT_TABLE_INFO = {
    "operation_achat": {
        "required_roles": [Roles.OC_SUPER_ADMIN.value],
        "values_mapping": {
            "statut": {
                1: "Saved",
                2: "Cancelled"
            }
        },
        "columns": {
            "id": "ID",
            "numero_declaration": "Numero de declaration",
            "date_declaration": "Date de declaration",
            "numero_bordereau": "Numero de bordereau",
            "date_bordereau": "Date de bordereau",
            "montant_global": "Montant global",
            "support_mad": "Support MAD",
            "statut": "Statut",
            "poc_id": "POC ID",
            "beneficiaire_pp_id": "Beneficiaire PP ID",
            "beneficiaire_pm_id": "Beneficiaire PM ID",
            "sous_operation_id": "Sous operation ID",
            "type_operation": "Type operation",
            "nom": "Nom",
            "prenom": "Prenom",
            "raison_sociale": "Raison sociale",
            "created_by": "Created by",
            "created_by_id": "Created by ID",
            "devise_labels": "Etiquettes de devise",
            "date_creation": "création de date"
        }
    }
}
