from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ticket_ids = fields.One2many('helpdesk.ticket', 'partner_id', string='Tickets')
