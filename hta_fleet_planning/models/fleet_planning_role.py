# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PlanningRole(models.Model):
    _inherit = "planning.role"
    
    vehicle_ids = fields.One2many('fleet.vehicle', 'planning_role_id', string="Vehicules")