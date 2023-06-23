from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Repair(models.Model):
    _inherit='repair.order'
    
    
    # vin=fields.Char(string="VIN")
    
    # mileage = fields.Float(string='Mileage')
    
    # registry_id=fields.Many2one(compute='_compute_based_on_vin',readonly=False)
    
    # partner_id=fields.Many2one(related='registry_id')
    
    # sale_order_id=fields.Many2one(related='registry_id')
    
    # product_id=fields.Many2one(related='registry_id')
    
    # @api.depends('vin')
    # def _compute_based_on_vin(self):
    #     motorcycle=self.env['motorcycle.registry'].search([('vin', '=', self.vin)])
    #     if motorcycle:
    #         self.registry_id=motorcycle['registry_id']
    #     else:
    #         raise ValidationError('Your VIN does not exist!')
        