import json

import werkzeug.wrappers
from odoo import http, _
from odoo.http import request


class RoomController(http.Controller):

    @http.route('/rooms', type='http', auth='public', method=['GET'])
    def index(self, **kwargs):
        rooms = http.request.env['hotel.room'].search([])
        ss = []
        for i in rooms:
            room = {
                'id': i.id,
                'name': i.name
            }
            ss.append(room)


        print(ss)
        return werkzeug.wrappers.Response(
            status=200,
            content_type='application/json;charset=utf-8',
            response={"name": ss},
        )