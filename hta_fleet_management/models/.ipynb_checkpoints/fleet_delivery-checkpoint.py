# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FleetDelivery(models.Model):
    _name = "fleet.delivery"
    _description = "Gestion des livraison"
    
    name = fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('loading', 'En chargement'),
        ('started', 'En cours'),
        ('done', 'Livre'),
        ('lock', 'Termine'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft'
    )
    partner_id = fields.Many2one('res.partner')
    delivery_line_ids = fields.One2many('fleet.delivery.line', 'delivery_id')
    partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', readonly=True, required=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    
class FleetDeliveryLine(models.Model):
    _name = "fleet.delivery.line"
    _description = "Gestion des livraison des commandes des clients"
    
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicule")
    delivery_id = fields.Many2one('fleet.delivery')
    product_id = fields.Many2one('product.product')
    product_quantity = fields.Float()
    

"""
class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"
    
"""