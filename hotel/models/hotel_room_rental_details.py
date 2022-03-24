from odoo import  fields, models, api
from datetime import datetime

class HotelRoomRentalDetail(models.Model):
    _name = 'hotel.room.rental.detail'
    _description = "Hotel room rental detail"

    room_id = fields.Many2one('hotel.room', string='Room')
    arrival_date = fields.Date(string="Arrival Date", default=datetime.today())
    departure_date = fields.Date(string="Departure Date", default=datetime.today())
    promotion_ids = fields.Many2many('hotel.promotion', string="Promotions")
    total = fields.Float(string="Total money", compute="_compute_total")

    @api.depends('promotion_ids','arrival_date','departure_date')
    def _compute_total(self):
        self.total = (self.departure_date - self.arrival_date).days * self.room_id.price
        money = self.total
        for record in self.promotion_ids:
            money = ((100-record.discount)/100)*self.money
        self.total = money


