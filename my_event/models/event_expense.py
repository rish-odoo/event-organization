from odoo import api, models, fields


class EventExpence(models.Model):
    _name="event.expense"
    _description = "Event total expense"

    event_id = fields.Many2one()
    expense_type = fields.One2many()
    amount = fields.float()
    vendor = fields.char()
    # Field	Type
    # event_id	Many2one
    # expense_type	Selection (Venue / Food / Travel / Marketing)
    # amount	Float
    # vendor	Char