from odoo import api,fields,models
from odoo.exceptions import ValidationError

class Repair(models.Model):
    _inherit='repair.order'
    
    vin=fields.Char(string="VIN")
    mileage=fields.Float(string="Current Mileage")
    registry_id=fields.Many2one(comodel_name="motorcycle.registry",compute="_get_based_on_vin")
    partner_id=fields.Many2one(related="registry_id")
    sale_order_id=fields.Many2one(related="registry_id")
    product_id=fields.Many2one(related="registry_id")
    
    @api.depends("vin")
    def _get_based_on_vin(self):
        motorcycle=self.env['motorcycle.registr'].search(['vin','=',self.vin])
        if motorcycle:
            self.registry_id=motorcycle
        else:
            raise ValidationError('VIN does not exist')    
        