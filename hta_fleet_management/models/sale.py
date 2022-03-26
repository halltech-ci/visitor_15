# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit="sale.order"
    
    
    #delivery = fields.Many2many('fleet.delivery', compute='_compute_fleet_delivery')
    delivery_count = fields.Integer(compute="_compute_delivery_line")
    
    """
    def _compute_fleet_delivery(self):
        for rec in self:
            rec.delivery_ld = self.env['fleet.delivery'].search([('order_id', '=', rec.id)]).id
    """        
    
    def _compute_delivery_line(self):
        for rec in self:
            lines = self.env['fleet.delivery'].search([('order_id', '=', rec.id)]).delivery_line_ids
            rec.delivery_count = len(lines)