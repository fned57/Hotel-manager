from odoo import  fields, models, api


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = "Hotel Rooms"

    name = fields.Char(string= "Name room")
    status = fields.Selection([ ('1', 'Empty'),('2', 'Busy')],'Type', default='1')
    description = fields.Text(string="Description Room")
    avatar = fields.Binary(string="Image Avatar")
    room_type_id = fields.Many2one('hotel.room.type', string="Room type")
    reservation_form_ids = fields.Many2many('hotel.reservation.form')

    @api.model
    def create(self, value):
        print(value)
