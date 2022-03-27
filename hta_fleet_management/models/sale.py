# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit="sale.order"
    
    
    delivery_lines = fields.One2many('fleet.delivery.line', 'sale_delivery_id',)
    delivery_count = fields.Integer(compute="_compute_delivery_line") 
    
    @api.depends('delivery_lines')
    def _compute_delivery_line(self):
        for rec in self:
            lines = rec.delivery_lines
            rec.delivery_count = len(lines)