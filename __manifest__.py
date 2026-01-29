{
    'name': 'Ritika`s Events',
    'summary': "Event App",
    'category': 'Tutorials',
    'maintainer' : "Ritika Shekhawat",
    'author': "Ritika",
    'depends': ['base', 'mail'],
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/event_security.xml',
        'views/event_services.xml',
        'views/event_type.xml',
        'views/event_venue.xml',
        'views/event_org_views.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ]
}
