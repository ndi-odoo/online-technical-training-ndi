# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """
        Academy module to manage training
        -courses
        -sessiones
        -attendees""",
    'author': "Odoo",
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'license':'LGPL-3',
    'data': [  
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo': [   
        'demo/academy_demo.xml'
    ]
    
}