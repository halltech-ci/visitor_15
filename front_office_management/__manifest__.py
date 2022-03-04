# -*- coding: utf-8 -*-


{
    'name': "Front Office Management",
    'version': '15.0.1.0.0',
    'summary': """Manage Front Office Operations:Visitors, Devices Carrying Register, Actions""",
    'description': """Helps You To Manage Front Office Operations, Odoo 15""",
    'author': "Cybrosys Techno Solutions",
    'maintainer': 'Cybrosys Techno Solutions',
    'company': "Cybrosys Techno Solutions",
    'website': "https://www.cybrosys.com",
    'category': 'Industries',
    'depends': ['base', 'hr'],
    'data': [
        'views/fo_visit.xml',
        'views/fo_visitor.xml',
        'views/fo_property_counter.xml',
        'report/report.xml',
        'report/fo_property_label.xml',
        'report/fo_visitor_label.xml',
        'report/visitors_report.xml',
        'security/fo_security.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
