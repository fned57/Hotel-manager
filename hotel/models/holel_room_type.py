from odoo import  fields, models, api


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = "Hotel Rooms Type"

    name = fields.Char(string="Room type")
    description = fields.Text("Description room type")
    price = fields.Float(string="Price Room")
    price_hour = fields.Float(string="Price Hour")
    price_overnight = fields.Float(string="Price over night")
    room_ids = fields.One2many('hotel.room', 'room_type_id', string="Rooms")

    @api.onchange("name")
    def _onchange_name(self):
        self.name = self.room_ids

    @api.depends('name')
    def _compute_name(self):
        self.name = self.room_ids