from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _inherit = ['mail.thread']

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    tag_ids = fields.Many2many(string="Tags", comodel_name='helpdesk.ticket.tag')
    partner_id = fields.Many2one(comodel_name='res.partner', string="Customer")
    phone = fields.Char(related = 'partner_id.phone', string='Phone')
    email = fields.Char(related = 'partner_id.email', string='Email')
    active = fields.Boolean('Active', default=True)
    stage = fields.Selection([
        ('new', 'New'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
        ], string='Stage', default="new")
    date_deadline = fields.Date(string="Deadline", default=fields.Date.today())
    count_days= fields.Integer(string="Days",compute='compute_days')
    user_id= fields.Many2one(comodel_name="res.users", string="Assigned to")
    login_manager = fields.Boolean('Is Helpdesk Manager', compute='compute_manager')

    @api.depends('date_deadline')
    def compute_days(self):
        today = fields.Date.today()
        for ticket in self:
            ticket.count_days = (ticket.date_deadline - today).days

    def stage_new(self):
        self.write({'stage': 'new'})

    def stage_in_progress(self):
        self.write({'stage': 'inprogress'})

    def stage_done(self):
        self.write({'stage': 'done'})

    def action_open_wizard(self):
        return {
            'name': 'Assign to',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'helpdesk.assign.wizard',
            'target': 'new',
            'context': self.env.context,
        }

    def assign_self(self):
        self.write({'user_id': self.env.user})

    @api.depends('date_deadline')
    def compute_manager(self):
        for ticket in self:
            if ticket.env.user.has_group('helpdesk.group_helpdesk_manager'):
                ticket.login_manager = True
            else:
                ticket.login_manager = False
