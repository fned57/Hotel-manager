from odoo import  fields, models


class hotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = "Hotel Rooms Type"

    name = fields.Char(string="Room type")
    description = fields.Text("Description room type")
    price = fields.Float(string="Price Room")
    avatar = fields.Binary(string="Image Avatar")



    