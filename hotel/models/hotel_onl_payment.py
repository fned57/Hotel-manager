from odoo import  fields, models


class hotelEvaluate(models.Model):
    _name = 'hotel.onl.payment'
    _description = "Hotel onl payment"

    id_guest = fields.Many2one('hotel.guest', string="Guest")
    id_reservation_form = fields.Many2one('hotel.reservation.form', string="Reservation from")
    total_amount = fields.Float(string="Total Amount")
    data_of_payment = fields.Date(string="Date of payment")
