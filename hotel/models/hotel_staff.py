from odoo import  fields, models


class hotelStaff(models.Model):
    _name = 'hotel.staff'
    _description = "Hotel staff"

    name = fields.Char(string="Name")
    birthday = fields.Date(string="Date of birth")
    address = fields.Char(string="Address")
    id_title = fields.Many2one('hotel.staff', string="Title")
    password = fields.Char(string="Password")
