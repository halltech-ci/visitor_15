# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class FleetDelivery(models.Model):
    _name = "fleet.delivery"
    _inherit = ['mail.thread']
    _description = "Gestion des livraison"
    
    name = fields.Char(index=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('loading', 'En chargement'),
        ('started', 'En cours'),
        ('done', 'Livre'),
        ('lock', 'Termine'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=True, default='draft'
    )
    partner_id = fields.Many2one('res.partner', string='Client')
    """partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', required=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )"""
    delivery_line_ids = fields.One2many('fleet.delivery.line', 'delivery_id')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    date = fields.Datetime(string='Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date")
    expected_date = fields.Date(string='Expected Date', required=True, copy=False,)
    
    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date']))
            vals['name'] = self.env['ir.sequence'].next_by_code('fleet.delivery.code', sequence_date=seq_date) or _('New')
        result = super(FleetDelivery, self).create(vals)
        return result

class FleetDeliveryLine(models.Model):
    _name = "fleet.delivery.line"
    _description = "Gestion des livraison des commandes des clients"
    state = fields.Selection(related="delivery_id.state")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicule")
    delivery_id = fields.Many2one('fleet.delivery')
    product_id = fields.Many2one('product.product')
    product_qty = fields.Float()
    date = fields.Datetime(related="delivery_id.date")
    delivery_date = fields.Date(string="Date de livraison")
    partner_id = fields.Many2one('res.partner', related="delivery_id.partner_id", string="Client")
    loading_date = fields.Datetime(string="Date de chargement")
    vehicle_owner = fields.Many2one('res.partner', related="vehicle_id.partner_id", string="Fournisseur")
    
class FleetVehicleDriver(models.Model):
    _name = "fleet.vehicle.driver"
    _description = "Manage all driver"
    
    name = fields.Char()
    driver_license = fields.Char(string="N° Permis de conduire")
    driver_license_cat = fields.Selection([('B', 'Permis B'), ('BCDE', 'Toute Categorie')])
    driver_contact = fields.Char(string="N° Téléphone")
    driver_company = fields.Many2one('res.partner', string='mployeur')
    driver_blood = fields.Selection(selection=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'),
                                              ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')]
    )
    
class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"
    
    #driver_id = fields.Many2one('fleet.vehicle.driver')
    partner_id = fields.Many2one('res.partner', string="Proprietaire")
    