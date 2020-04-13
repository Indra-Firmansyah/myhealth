
{
    'name': 'Beauty Spa Management',
    'summary': """Beauty Parlour Management with Online Booking System""",
    'version': '10.0.2.0.0',
    'author': 'Cybrosys Techno Solutions',
    'website': "http://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    "category": "Industries",
    'depends': ['base', 'account', 'mail', 'website'],
    'data': ['views/salon_holiday.xml',
             'views/salon_data.xml',
             'views/myhealth_chair.xml',
             'views/myhealth_services.xml',
             'views/salon_order_view.xml',
             'views/myhealth_dashboard.xml',
             'views/booking_backend.xml',
             'views/salon_bookings.xml',
             'views/salon_email_template.xml',
             'views/salon_config.xml',
             'views/working_hours.xml',
             'security/ir.model.access.csv',
             ],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
