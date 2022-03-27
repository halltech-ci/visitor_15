# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.tools import float_round, format_duration, float_compare, float_is_zero

class FleetDeliveryLine(models.Model):
    _inherit = 'fleet.delivery.line'
    
    planning_slot_ids = fields.One2many('planning.slot', 'fleet_delivery_line')
    planning_hours_planned = fields.Float(store=True, default=2.0)
    planning_hours_to_plan = fields.Float(store=True, default=2.0)
    state = fields.Selection(related="delivery_id.state")
    
    
    def name_get(self):
        result = []
        for line in self.sudo():
            name = '%s-%s' % (line.delivery_id.order_id.name, line.vehicle_id.name)
            result.append((line.id, name))
        return result
    
    def _post_process_planning_delivery_line(self, ids_to_exclude=None):
        """
            This method ensures unscheduled slot attached to a sale order line
            has the right allocated_hours and is unique

            This method is mandatory due to cyclic dependencies between planning.slot
            and sale.order.line models.

            :param ids_to_exclude: the ids of the slots already being recomputed/written.
        """
        sol_planning = self.filtered('vehicle_id.planning_enabled')
        if sol_planning:
            unscheduled_slots = self.env['planning.slot'].sudo().search([
                ('fleet_delivery_line', 'in', sol_planning.ids),#sale_line_id
                ('start_datetime', '=', False),
            ])
            sol_with_unscheduled_slot = set()
            slots_to_unlink = self.env['planning.slot']
            for slot in unscheduled_slots:
                if slot.fleet_delivery_line.id in sol_with_unscheduled_slot:#sale_line_id
                    # This slot has to be unlinked as an other exists for the
                    # same sale order line
                    # This 'unlink' will also avoid infinite loop
                    # => if there are 2 unscheduled slots for a sol,
                    # ==> then the first is written and triggers a recompute on the second
                    # ==> then the second is written and triggers a recompute on the first
                    slots_to_unlink |= slot
                else:
                    sol_with_unscheduled_slot.add(slot.fleet_delivery_line.id)#sale_line_id
                    if float_is_zero(slot.allocated_hours, precision_digits=2):
                        slots_to_unlink |= slot
            slots_to_unlink.unlink()

    
    
    
    
    