from odoo import  fields, models


class HotelBill(models.Model):
    _name = 'hotel.bill.detail'
    _description = "Hotel bill detail"

    id_bill = fields.Many2one('hotel.bill', string="Bill")
    room_cost = fields.Char(string="Room") # rethink
    service_cost = fields.Char(string="Service") # rethink
    promotion_discount = fields.Char(string="Promotion discount") # r ethink
    mode_of_payment = fields.Char(string="Mode id payment") # rethink
    amount = fields.Float(string="Amount")
