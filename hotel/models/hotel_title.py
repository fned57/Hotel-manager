from odoo import  fields, models


class hotelTitle(models.Model):
    _name = 'hotel.title'
    _description = "Hotel title"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description title")
