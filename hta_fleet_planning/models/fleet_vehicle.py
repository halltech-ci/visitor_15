# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
    
    planning_enabled = fields.Boolean('Plan Services', default=False)
    planning_role_id = fields.Many2one('planning.role')
    