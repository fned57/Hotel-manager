from odoo import  fields, models


class hotelPromotion(models.Model):
    _name = 'hotel.promotion'
    _description = "Hotel promotion"

    name = fields.Char(string="Name")
    short_description = fields.Text(string="Short description")
    subject = fields.Char(string="Subject")
    image = fields.Binary(string="Image promotion")
    starting_date = fields.Date(string="start date")
    ending_date = fields.Date(string="End Date")
    status = fields.Char(string="Status")
    id_type_room = fields.Many2one('hotel.type.room', string="Type room")
    