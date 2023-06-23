from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = ['motorcycle.registry']
    

    lot_ids = fields.One2many('stock.lot', 'registry_id', 'Lots')
    lot_id = fields.Many2one('stock.lot', 'Lot', compute='_compute_lot_id', store=True)

    related_order = fields.Many2one('sale.order', 'Order')

    #vin = fields.Char(related='lot_id.name', string='VIN', store=True)

    @api.depends('lot_ids')
    def _compute_lot_id(self):
        for record in self:
            if record.lot_ids:
                record.lot_id = record.lot_ids[0]

    @api.constrains('lot_ids')
    def _check_lot_ids(self):
        for record in self:
            if len(record.lot_ids) > 1:
                raise ValidationError("You cannot assign more than one lot to a motorcycle registry.")
