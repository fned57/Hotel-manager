from odoo import  fields, models


class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _description = "Hotel guest"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    idenitily = fields.Char(string="Indenitily")
    password = fields.Char(string="Password")
