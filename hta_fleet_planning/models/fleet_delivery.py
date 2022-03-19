# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FleetDelivery(models.Model):
    _inherit = "fleet.delivery"
    
    
    def action_delivery_plan(self):
        action = self.env["ir.actions.actions"]._for_xml_id("planning.fleet_delivery_action")
        action['views'] = [(False, 'form')]
        action['res_id'] = self.delivery.id
        return action