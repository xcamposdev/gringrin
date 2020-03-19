# -*- coding: utf-8 -*-
{
    'name': "sale_custom",

    'summary': """
        Generar etiquetas pedidos de venta""",

    'description': """
        Generar etiquetas pedidos de venta
    """,

    'author': "Develoop Software",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sales_team', 'payment', 'portal', 'utm'],

    # always loaded
    'data': [
        # report
        'reports/etiquetas_report.xml',
        'reports/etiquetas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}