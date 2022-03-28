from odoo import fields, models, api
from datetime import datetime


class HotelReservationForm(models.Model):
    _name = 'hotel.reservation.form'
    _description = "Hotel Reservation form"
    _rec_name = 'guest_id'

    guest_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user.id)
    date_of_issue = fields.Date(string="Date of issue", default=datetime.today())
    status = fields.Boolean(string='payment', default=False)
    total_mature = fields.Integer(string="Total mature")
    total_children = fields.Integer(string="Total children")
    room_ids = fields.One2many('hotel.room.rental.detail', 'reservation_id', string="List rooms")
    service_detail_ids = fields.One2many('hotel.service.detail', 'reservation_id', string="Service")
    money = fields.Float(string="Money")
    total_money = fields.Float(string="Total money", compute='_compute_total_many')

    @api.depends('room_ids', 'service_detail_ids')
    def _compute_total_many(self):
        total_room = 0.0
        total_service = 0.0
        for record in self:
            for room in record.room_ids:
                total_room += room.total
            for service in self.service_detail_ids:
                total_service += service.amount
        self.total_money = total_room + total_service

    def payment(self):
        self.status = True
        for record in self:
            if record.room_ids:
                for room in record.room_ids:
                    room.room_id.status = '1'

    @api.model
    def create(self, value):
        if('room_ids' in value):
            for room in value['room_ids']:
                self.env['hotel.room'].browse(room[2]['room_id']).status = '2'
        return super().create(value)


