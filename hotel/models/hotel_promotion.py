from odoo import  fields, models


class HotelPromotion(models.Model):
    _name = 'hotel.promotion'
    _description = "Hotel promotion"

    name = fields.Char(string="Name")
    short_description = fields.Text(string="Short description")
    subject = fields.Char(string="Subject")
    image = fields.Binary(string="Image promotion")
    starting_date = fields.Date(string="start date")
    discount = fields.Float(string="Discount")
    ending_date = fields.Date(string="End Date")
    status = fields.Char(string="Status")
    room_type_id = fields.Many2one('hotel.room.type', string="Room type")
    