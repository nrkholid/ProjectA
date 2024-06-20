{
    "name" : "PT. Sanbe Farma - Custom Contact",
    "description" : "Pelatihan Technical Odoo V17 untuk PT. Sanbe Farma",
    "author" : "PT. Sanbe Farma, PT. Arkana Solusi Digital",
    "version" : "17.0.1.0.0",
    "category" : "Others",
    "license" : "OPL-1",
    "depends" : [
        "base", 
        "contacts"
    ],
    "data" : [
        "security/ir.model.access.csv",
        "views/res_partner_inherit_view.xml",
    ],
    "auto_install" : False, 
    "installable" : True,
    "application" : True,
    "external_dependencies" : {"python" : []}
}