from odoo import  fields, models, api
from datetime import datetime


class HotelRoomRentalDetail(models.Model):
    _name = 'hotel.room.rental.detail'
    _description = "Hotel room rental detail"

    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    arrival_date = fields.Date(string="Arrival Date", default=datetime.today(), required=True)
    departure_date = fields.Date(string="Departure Date", default=datetime.today(), required=True)
    promotion_ids = fields.Many2many('hotel.promotion', string="Promotions")
    total = fields.Float(string="Total money")

    @api.onchange('promotion_ids', 'arrival_date', 'departure_date', "room_id")
    def _onchange_total(self):
        day_uses = (self.departure_date - self.arrival_date).days
        money = self.room_id.price * int(day_uses)
        for record in self.promotion_ids:
            money = ((100-record.discount)/100)*money
        self.total = money








