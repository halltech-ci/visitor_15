# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PlanningSlot(models.Model):
    _inherit = "planning.slot"
    
    fleet_delivery_line = fields.Many2one("fleet.delivery.line", string="Delivery Line")
    delivery_id = fields.Many2one('fleet.delivery', string='Fleet Delivery', related='fleet_delivery_line.delivery_id', store=True)
    delivery_line_plannable = fields.Boolean(related='fleet_delivery_line.vehicle_id.planning_enabled')
    
    
    def action_view_fleet_delivery(self):
        action = self.env["ir.actions.actions"]._for_xml_id("hta_fleet_management.fleet_delivery_action")
        action['views'] = [(False, 'form')]
        action['res_id'] = self.delivery.id
        return action