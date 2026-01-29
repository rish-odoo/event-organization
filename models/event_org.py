import datetime
from odoo import api, models, fields
from odoo.exceptions import UserError


class event_org(models.Model):
    _name = "event.org"
    _inherit ='mail.thread'
    _description = "Make your Event"
    _order="name"

    name = fields.Char("Event name")
    active=fields.Boolean("Active")
    custmer=fields.Char("Custmer Name")
    cu_m_no=fields.Integer("Custmer Mobile Number")
    cu_m_email=fields.Char("custmer Email")
    description = fields.Text("Description")
    budget = fields.Float("Your Budget")
    venue = fields.Selection([('G', 'Garden'), ('H', 'Hall'),
                             ('Hotel', 'Hotel'), ('re', 'Resturent'), ('cafe', 'Cafe')])
    other_venue=fields.Many2one("event.venue",string="other Venue")
    attendees = fields.Integer("Number of Maximum Attendee")
    state = fields.Selection(
        [('Co', 'Confirm'), ('O', 'Ongoing'), ('D', 'Done'),('C', 'Cancle'),('N', 'New')])
    start_date=fields.Date("Date from")
    end_date=fields.Date("Date to")
    event_type_id = fields.Many2one("event.type", string="Event-Type")
    service_ids=fields.One2many('event.services','ser_id')
    total_days=fields.Integer("Total Days",compute="calculate_days",store=True)

    _sql_constraints = [
        ('check_budget', 'CHECK (budget > 5000)', 'Bugget should be Greater Than 5000')]

    def calculate_days(self):
        for record in self:
            if record.start_date and record.end_date:
                days = (record.end_date - record.start_date).days
                record.total_days = days
                print(days)

    def action_confirm(self):
        if self.state == 'Co':
            self.state = "Co"
        else:
            self.state="C"

    def action_cancel(self):
        if self.state == 'C':
            self.state = "C"
        else :
            self.state="Co"

    def action_ongoing(self):
        if self.state == 'O':
            self.state = "O"
        else:
            self.state="CO"

    def action_ongoing(self):
        if self.state == 'D':
            self.state = "D"
        else:
            self.state="CO"

    def action_new(self):
        if self.state == 'N':
            self.state = "N"
        else:
            self.state="CO"


