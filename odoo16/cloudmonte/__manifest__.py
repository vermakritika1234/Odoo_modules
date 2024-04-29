{
    'name': 'CloudMonte Assignment',
    'version': '1.0',
    'category': 'Customization',
    'author': 'Cloud monte',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_form.xml',
        # 'views/res_partner_form.xml',
        # 'report/sale_order_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
}
