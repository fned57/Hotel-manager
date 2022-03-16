from odoo import  fields, models


class hotelService(models.Model):
    _name = 'hotel.service'
    _description = "Hotel Service"

    name = fields.Char(string= "Name service")
    price = fields.Float(string="Price")
    description = fields.Text(string="Description Room")
    date_of_payment = fields.Char(string="Date of payment")