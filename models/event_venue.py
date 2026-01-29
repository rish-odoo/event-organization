from odoo import api, fields, models


class EventVenue(models.Model):
    _name = "event.venue"
    _description = 'Venue selection'
    _order="name"

    
    Event_name= fields.One2many("event.org","other_venue",string="Event Name")
    
    name=fields.Char("name")
    garden=fields.Boolean("Garden")
    hall=fields.Boolean("Hall")
    hotel=fields.Boolean("Hotel")
    restaurants=fields.Boolean("Restaurants")
    cafe=fields.Boolean("Cafe")
    ven_charg_for_garden=fields.Float("Garden Charges",compute="_compute__garden",readonly=False)
    ven_charg_for_hall=fields.Float("Hall Charges",compute="_compute__hall",readonly=False)
    ven_charg_for_cafe=fields.Float("Cafe Charges",compute="_compute__cafe",readonly=False)
    ven_charg_for_hotel=fields.Float("Hotel Charges",compute="_compute__hotel",readonly=False) 
    ven_charg_for_res=fields.Float("Restaurants Charges",compute="_compute__restaurants",readonly=False)
    rooms=fields.Integer("Required Rooms")
    cost_per_day = fields.Integer("Cost per day")
    hall_capisity=fields.Integer("Hall Required")
    location=fields.Char("Address of venue")
    capisity=fields.Integer("capisity")
    date_availibilty=fields.Datetime("Available From")
    _sql_constraints = [('check_ven_charg_for_garden', 'CHECK (ven_charg_for_garden > 150000)', 'A Garden Charges is greater than 150000'),
                        ('check_ven_charg_for_hall', 'CHECK (ven_charg_for_hall > 5000)', 'A Hall Charges is Greater than 5000')]

    
    @api.depends("garden")
    def _compute__garden(self):
        for g in self:
            if g.garden:
                g.ven_charg_for_garden = 200000
            else:
                g.ven_charg_for_garden=0

            
    @api.depends("hall")
    def _compute__hall(self):
        for g in self:
            if g.hall:
                g.ven_charg_for_hall = 200
            else:
                g.ven_charg_for_hall=0
   
    @api.depends("hotel")
    def _compute__hotel(self):
        for g in self:
            if g.hotel:
                g.ven_charg_for_hotel = 20
            else:
                g.ven_charg_for_hotel=0
 
    @api.depends("restaurants")
    def _compute__restaurants(self):
        for g in self:
            if g.restaurants:
                g.ven_charg_for_res = 100000
            else:
                g.ven_charg_for_res=0
  
    
    @api.depends("cafe")
    def _compute__cafe(self):
        for g in self:
            if g.cafe:
                g.ven_charg_for_cafe = 400000
            else:
                g.ven_charg_for_cafe=0
