from odoo import fields, models


class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.tag"
    _description = "Ticket tags"
    _rec_name = "tag"

    tag = fields.Char(string='Tag')
