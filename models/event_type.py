from odoo import models, fields


class event_type(models.Model):
    
    _name = "event.type"
    _description = "Event Type"
    _order = "sequence"

    name = fields.Char("Name of Event")
    Start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    event_ids=fields.One2many("event.org","event_type_id",string="Event Type")
    sequence = fields.Integer('Sequence')


