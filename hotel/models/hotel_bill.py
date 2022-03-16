from odoo import  fields, models


class hotelBill(models.Model):
    _name = 'hotel.bill'
    _description = "Hotel bill"

    date = fields.Date(string="Date")
    id_staff = fields.Many2one('hotel.staff', string="Staff")
    cost = fields.Float(string="Cost")
    # id_purchase_order =
