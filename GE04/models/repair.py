from odoo import api,fields,models

class Repair(models.Model):
    _inherit='repair.order'
    
    vin=fields.Char(string="VIN")
    mileage=fields.Float(string="Current Mileage")
    registry_id=fields.Many2one(comodel_name="motorcycle.registry",compute="_get_based_on_vin", store=True)
    partner_id=fields.Many2one(relation="registry_id")
    sale_order_id=fields.Many2one(relation="registry_id")
    product_id=fields.Many2one(relation="registry_id")
    
    @api.depends("vin")
    def _get_based_on_vin(self):
        for record in self:
            motorcycle=record.env['motorcycle.registry'].search([('vin','=',record.vin)])
            if motorcycle:
                record.registry_id=motorcycle
            else:
                record.registry_id=False   
        