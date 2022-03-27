# -*- coding: utf-8 -*-
# from odoo import http


# class HtaFleetPlanning(http.Controller):
#     @http.route('/hta_fleet_planning/hta_fleet_planning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_fleet_planning/hta_fleet_planning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_fleet_planning.listing', {
#             'root': '/hta_fleet_planning/hta_fleet_planning',
#             'objects': http.request.env['hta_fleet_planning.hta_fleet_planning'].search([]),
#         })

#     @http.route('/hta_fleet_planning/hta_fleet_planning/objects/<model("hta_fleet_planning.hta_fleet_planning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_fleet_planning.object', {
#             'object': obj
#         })
