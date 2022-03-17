from odoo import  fields, models


class HotelReservationForm(models.Model):
    _name = 'hotel.reservation.form'
    _description = "Hotel Reservation form"

    id_guest = fields.Many2one('hotel.guest', string="Guest")
    date_of_issue = fields.Date(string="Date of issue")
    status = fields.Char(string="Status")
    arrival_date= fields.Date(string="Arrival Date")
    departure_date = fields.Date(string="Departure Date")
    total_mature = fields.Integer(string="Total mature")
    total_chidren = fields.Integer(string="Total chidren")
    id_type_room = fields.Many2one('hotel.room.type', string="Room Type")
    room_ids = fields.Many2many('hotel.room', string="List rooms")
