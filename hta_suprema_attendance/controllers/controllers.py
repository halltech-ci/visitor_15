# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSupremaAttendance(http.Controller):
#     @http.route('/hta_suprema_attendance/hta_suprema_attendance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_suprema_attendance/hta_suprema_attendance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_suprema_attendance.listing', {
#             'root': '/hta_suprema_attendance/hta_suprema_attendance',
#             'objects': http.request.env['hta_suprema_attendance.hta_suprema_attendance'].search([]),
#         })

#     @http.route('/hta_suprema_attendance/hta_suprema_attendance/objects/<model("hta_suprema_attendance.hta_suprema_attendance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_suprema_attendance.object', {
#             'object': obj
#         })
