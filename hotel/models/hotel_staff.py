from odoo import  fields, models


class HotelStaff(models.Model):
    _name = 'hotel.staff'
    _description = "Hotel staff"

    name = fields.Char(string="Name")
    birthday = fields.Date(string="Date of birth")
    address = fields.Char(string="Address")
    position= fields.Many2one('hotel.position', string="Position")
    password = fields.Char(string="Password")

