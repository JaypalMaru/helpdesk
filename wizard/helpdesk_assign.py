from odoo import fields, models


class HelpdeskAssign(models.TransientModel):
    _name = 'helpdesk.assign.wizard'
    _description = 'Assign tickets wizard'

    user_id = fields.Many2one('res.users', string='User')

    def assign_to(self):
        self.env['helpdesk.ticket'].browse(self.env.context['active_ids']).write({'user_id':self.user_id})
