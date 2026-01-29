from odoo import api, fields, models


class event_services(models.Model):
    _name = "event.services"
    _description = 'Event services'
    _order="ammount desc"


    services= fields.Selection([('Cat','Catering'), ('dec', 'Decoration'), ('ph', 'Photography'),('st','Staff')])
    status=fields.Selection([('Co','Confirm'),('C','Cancle')])
    ammount=fields.Float("Amount")
    total=fields.Float('Sub Total')
    ser_id=fields.Many2one("event.org")  
    vender = fields.Many2one("res.partner", string="vender")
    menue = fields.Char("Make list of Menue")
    seating=fields.Selection([('b',"buffet"),('s',"sit-down"),('d',"dining")],string="seating arrangment",default="b")
    attendee=fields.Integer("Number of Guest")

    staff_member=fields.Integer("How many Staff needed",default=10)
    staff_total=fields.Float("Staff Total charges",compute="_compute_staff_total")

    catring_total=fields.Float("catring charges",compute="_compute_catring_total")
    days=fields.Float("Number of days for this service")
    per_person_charges=fields.Float("per person charges for this service")
    
    dec_charges=fields.Float("Decoration Charges")
    ph_charges=fields.Float("photography Charges")
     
    sub_total = fields.Float("Sub Total")
   
    @api.depends('services','attendee','days','per_person_charges')
    def _compute_catring_total(self):
        for i in self:
            if i.services == 'Cat':
               i.catring_total = i.attendee*i.days*i.per_person_charges
            else:
                i.catring_total=0
           
     
    @api.depends('services','staff_member','days','per_person_charges')
    def _compute_staff_total(self):
        for i in self:
            if i.services == 'st':
               i.staff_total = (i.staff_member)*(i.days)*(i.per_person_charges)
            else :
                i.services == ''
                i.staff_total = 0

