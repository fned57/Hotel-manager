from odoo import  fields, models


class HotelServiceDetail(models.Model):
    _name = 'hotel.service.detail'
    _description = "Hotel Service detail"

    id_service = fields.Many2one('hotel.service', string="Service")
    # id
    number_of_uses = fields.Integer(string=" Number of Uses")
    amount = fields.Float(string="Amount")
    note = fields.Text(string="Node")