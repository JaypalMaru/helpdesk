{
    'name': 'Helpdesk',
    'category': 'Services/Helpdesk',
    'description': """
Allow users to manage ticket.
""",
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_tag_views.xml',
        'views/res_partner_views.xml',
        'wizard/helpdesk_assign_views.xml',
    ],
    'depends': ['mail'],
}
