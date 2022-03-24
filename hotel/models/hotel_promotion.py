from odoo import  fields, models, api
from datetime import date

class HotelPromotion(models.Model):
    _name = 'hotel.promotion'
    _description = "Hotel promotion"

    name = fields.Char(string="Name")
    short_description = fields.Text(string="Short description")
    subject = fields.Char(string="Subject")
    image = fields.Binary(string="Image promotion")
    starting_date = fields.Date(string="start date", default=date.today())
    discount = fields.Float(string="Discount")
    ending_date = fields.Date(string="End Date", default=date.today())
    room_type_id = fields.Many2one('hotel.room.type', string="Room type")
    status = fields.Selection([('1', 'Empty'), ('2', 'Busy')], 'Status', default='2')

    # @api.onchange('starting_date', 'ending_date')
    # def _compute_status(self):
    #     if ((date.today() - self.starting_date).days >= 0) and ((date.today() - self.ending_date).days <= 0):
    #         self.status = 1
    #     else:
    #         self.status = 2

    