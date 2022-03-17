from odoo import  fields, models


class HotelEvaluate(models.Model):
    _name = 'hotel.evaluate'
    _description = "Hotel evaluate"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    subject = fields.Char(string="Subject")
    guest = fields.Char(string="Guest")
    date_sent = fields.Date(string="Data sent")
    room_type_id = fields.Many2one('hotel.room.type', string="Room type")
