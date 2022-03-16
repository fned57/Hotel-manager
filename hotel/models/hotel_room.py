from odoo import  fields, models


class hotelRoom(models.Model):
    _name = 'hotel.room'
    _description = "Hotel Rooms"

    name = fields.Char(string= "Name room")
    status = fields.Selection([ ('1', 'Empty'),('2', 'Busy')],'Type', default='1')
    description = fields.Text(string="Description Room")
    # room_type_id = fields.One2many()