from odoo import  fields, models, api

from datetime import datetime
class HotelReservationForm(models.Model):
    _name = 'hotel.reservation.form'
    _description = "Hotel Reservation form"
    _rec_name = 'guest_id'

    guest_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user.id)
    date_of_issue = fields.Date(string="Date of issue", default=datetime.today())
    status = fields.Selection([('1','thanh toans'),('2','Chua thanh toan')], default='2')
    total_mature = fields.Integer(string="Total mature")
    total_chidren = fields.Integer(string="Total chidren")
    room_ids = fields.Many2many('hotel.room.rental.detail', string="List rooms")
    service_detail_ids = fields.Many2many('hotel.service.detail', string="Service")
    money = fields.Float(string="Money")
    total_money = fields.Float(string="Total money", compute='_compute_total_many')

    @api.depends('room_ids','service_detail_ids')
    def _compute_total_many(self):
        self.total_money = 1
        # total_room = 0.0
        # total_service = 0.0
        # for record in self:
        #     for room in record.room_ids:
        #         total_room += room.total
        #     for service in self.service_detail_ids:
        #         total_service += service.amount
        # self.total_money = total_room + total_service

    def payment(self):
        self.status = '1'

