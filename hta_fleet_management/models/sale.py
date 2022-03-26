# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit="sale.order"
    
    delivery_count = fields.Integer(compute="_compute_delivery_line")
    
    def _compute_delivery_line(self):
        for rec in self:
            lines = self.env['fleet.delivery'].search([('order_id', '=', rec.id)]).delivery_line_ids
            rec.delivery_count = len(lines)