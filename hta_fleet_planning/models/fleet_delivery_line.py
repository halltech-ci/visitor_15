# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.tools import float_round, format_duration, float_compare, float_is_zero

class FleetDeliveryLine(models.Model):
    _inherit = 'fleet.delivery.line'
    
    planning_slot_ids = fields.One2many('planning.slot', 'fleet_delivery_line')
    planning_hours_planned = fields.Float(store=True, default=2.0)
    planning_hours_to_plan = fields.Float(store=True, default=2.0)
    state = fields.Selection(related="delivery_id.state")
    
    
    def name_get(self):
        result = []
        for line in self.sudo():
            name = '%s-%s' % (line.delivery_id.order_id, line.vehicle_id.name)
            result.append((line.id, name))
        return resul
    
    
    
    
    