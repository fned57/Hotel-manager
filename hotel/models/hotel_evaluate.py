from odoo import  fields, models


class hotelEvaluate(models.Model):
    _name = 'hotel.evaluate'
    _description = "Hotel evaluate"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    subject = fields.Char(string="Subject")
    guest = fields.Char(string="Guest")
    date_sent = fields.Date(string="Data sent")
    id_type_room = fields.Many2one('hotel.type.room', string="Type room")
