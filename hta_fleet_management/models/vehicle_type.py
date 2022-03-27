# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ParkingVehiculeType(models.Model):
    _name ="parking.vehicle.type"
    _description = "All type of vehicle"
    
    name = fields.Char()
    