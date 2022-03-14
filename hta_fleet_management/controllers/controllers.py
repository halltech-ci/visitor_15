# -*- coding: utf-8 -*-
# from odoo import http


# class HtaFleetManagement(http.Controller):
#     @http.route('/hta_fleet_management/hta_fleet_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_fleet_management/hta_fleet_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_fleet_management.listing', {
#             'root': '/hta_fleet_management/hta_fleet_management',
#             'objects': http.request.env['hta_fleet_management.hta_fleet_management'].search([]),
#         })

#     @http.route('/hta_fleet_management/hta_fleet_management/objects/<model("hta_fleet_management.hta_fleet_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_fleet_management.object', {
#             'object': obj
#         })
