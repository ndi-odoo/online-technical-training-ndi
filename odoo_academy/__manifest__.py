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
    'depends': ['base'],
    'license':'LGPL-3',
    'data': [  
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml'
    ],
    'demo': [   
        'demo/academy_demo.xml'
    ]
    
}