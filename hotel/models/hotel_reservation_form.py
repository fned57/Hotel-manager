from odoo import  fields, models, api

from datetime import datetime
class HotelReservationForm(models.Model):
    _name = 'hotel.reservation.form'
    _description = "Hotel Reservation form"
    _rec_name = 'guest_id'

    guest_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user.id)
    date_of_issue = fields.Date(string="Date of issue", default=datetime.today())
    status = fields.Char(string="Status")
    arrival_date = fields.Date(string="Arrival Date")
    departure_date = fields.Date(string="Departure Date")
    total_mature = fields.Integer(string="Total mature")
    total_chidren = fields.Integer(string="Total chidren")
    total_many = fields.Float(string="Total many", compute='_compute_total_many')
    room_ids = fields.Many2many('hotel.room', string="List rooms")
    service_detail_ids = fields.Many2many('hotel.service.detail', string="Service")
    # bill_ids = fields.One2many('hotel.bill.detail', 'reservation_form_id', string='bill line')

    @api.depends('room_ids','service_detail_ids')
    def _compute_total_many(self):
        total_room = 0.0
        total_service = 0.0
        for record in self:
            for room in record.room_ids:
                total_room += room.room_type_id.price
            for service in self.service_detail_ids:
                total_service += service.amount
        self.total_many= total_room + total_service

