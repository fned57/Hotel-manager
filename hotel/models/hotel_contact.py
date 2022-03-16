from odoo import  fields, models


class hotelContact(models.Model):
    _name = 'hotel.contact'
    _description = "Hotel cantact"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    subject = fields.Text(string="Subject")
    date_sent = fields.Date(string="Date Sent")
    status = fields.Char(string="Status")

