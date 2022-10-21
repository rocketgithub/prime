# -*- coding: utf-8 -*-
{
    'name': "Prime",

    'summary': """ Prime """,

    'description': """
        Módulo con funcionalidades para Prime
    """,

    'author': "Aquih",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','product'],

    'data': [
        'views/product_template_views.xml',
        'views/product_views.xml',
        'views/sale_views.xml',
        'security/sale_security.xml',
    ],
}
