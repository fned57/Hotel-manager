# -*- coding: utf-8 -*-
{
    'name': "Hotel",
    'summary': """""",
    'description': """""",
    'author': "Trần Đăng Tuấn",
    'website': "https://fb.com/tdthc",
    'category': '',
    'version': '0.1',
    'depends': [

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_view.xml',
        'views/hotel_menu_root.xml',
        'views/hotel_room_type_view.xml',
        'views/hotel_promotion_view.xml',
        'views/hotel_evaluate_view.xml',
        'views/hotel_service_view.xml',
        'views/hotel_service_detail_view.xml',
        'views/hotel_position_view.xml',
        'views/hotel_staff_view.xml',
        'views/hotel_guest_view.xml',
        'views/hotel_reservation_form_view.xml',
        'views/hotel_onl_payment_view.xml',
        'views/hotel_bill_view.xml',
        'views/hotel_bill_detail_view.xml',


    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
