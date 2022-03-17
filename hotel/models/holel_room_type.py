from odoo import  fields, models


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = "Hotel Rooms Type"

    name = fields.Char(string="Room type")
    description = fields.Text("Description room type")
    price = fields.Float(string="Price Room")
    room_ids = fields.One2many('hotel.room','room_type_id',string="Rooms")



    