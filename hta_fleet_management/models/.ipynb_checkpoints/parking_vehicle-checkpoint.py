# -*- coding: utf-8 -*-

from odoo import models, fields, api


VEHICLE_TYPE = [('voiture', 'Voiture'), ('camion', 'Camion'), ('camionnette', 'Camionnette'), ('moto', 'Moto')]

class ParckingVehicle(models.Model):
    _name = "parking.vehicle"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Manage enterprise car fleet"
    
    name = fields.Char(string="Immatriculation")
    description = fields.Html("Vehicle Description", help="Add a note about this vehicle")
    mineral_plate = fields.Char(required=True)
    vehicle_type = fields.Selection(selection = VEHICLE_TYPE, default='camion')
    #transmission = 
    partner_id = fields.Many2one('res.partner')
    

class ParkingVehicleModel(models.Model):
    _name = "vehicle.modele"
    _description = "All vehicle model"
    
    name = fields.Char()
    description = fields.Html("Vehicle Description", help="Add a note about this vehicle")
    transmission = fields.Selection([('manual', 'Manual'), ('automatic', 'Automatic')], 'Transmission', help='Transmission Used by the vehicle')
    power = fields.Integer('Puissance')
    
    
    
    
    
    
    