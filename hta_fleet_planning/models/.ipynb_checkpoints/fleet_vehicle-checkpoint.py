# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
    
    planning_enabled = fields.Boolean('Plan Services', default=False)
    planning_role_id = fields.Many2one('planning.role')
    

class PlanningSlot(models.Model):
    _inherit = "planning.slot"
    
    fleet_delivery_line = fields.Many2one("fleet.delivery.line", string="Delivery Line")
    delivery_id = fields.Many2one('fleet.delivery', string='Fleet Delivery', related='fleet_delivery_line.delivery_id', store=True)
    delivery_line_plannable = fields.Boolean(related='fleet_delivery_line.vehicle_id.planning_enabled')
    
    
    def action_view_sale_order(self):
        action = self.env["ir.actions.actions"]._for_xml_id("sale.action_orders")
        action['views'] = [(False, 'form')]
        action['res_id'] = self.sale_order_id.id
        return action