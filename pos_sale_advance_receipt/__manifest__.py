# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'POS Sale Order Advanced Receipt',
    'version': '1.1',
    'category': 'sale',
    'sequence': 10,
    'summary': 'Customization of POS Sale Order Advanced Receipt',
    'description': """
    'author': 'Muhammad Usman',
""",
    'depends': ['point_of_sale', 'sale_management', 'pos_sale'],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        'point_of_sale.assets': [
        ],
        'web.assets_qweb': [
            'pos_sale_advance_receipt/static/src/xml/**/*',
        ],
    },
}
