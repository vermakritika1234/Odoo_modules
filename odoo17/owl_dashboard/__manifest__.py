# -*- coding: utf-8 -*-
{
    'name': "owl_dashboard",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','web','board'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/main.xml',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    'assets': {
   'web.assets_backend': [
       'owl_dashboard/static/src/js/sales_dashboard.js',
       'owl_dashboard/static/src/xml/sales_dashboard.xml',
    #    'owl_dashboard/static/src/kpi_card/kpi_cards.xml',
    #    'owl_dashboard/static/src/kpi_card/kpi_cards.js',

   ],
},
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

