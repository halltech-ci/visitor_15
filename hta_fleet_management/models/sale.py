# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit="sale.order"
    
    
    delivery_lines = fields.One2many('fleet.delivery.line', 'sale_delivery_id',)
    delivery_count = fields.Integer(compute="_compute_delivery_line", string='Livraisons') 
    
    @api.depends('delivery_lines')
    def _compute_delivery_line(self):
        for rec in self:
            lines = rec.delivery_lines
            rec.delivery_count = len(lines)
            
    
    def action_open_fleet_delivery(self):
        self.ensure_one()
        delivery_lines = self.env['fleet.delivery.line'].search([
            ('id', 'in', self.delivery_lines.ids)])

        return {
            "type": "ir.actions.act_window",
            "res_model": "fleet.delivery.line",
            "views": [[False, "tree"]],
            "domain": [("id", "in", delivery_lines.ids)],
            "context": dict(self._context, create=False),
            "name": "Detail des livraisons",
        }