from odoo import api,fields,models

class StockLot(models.Model):
    
    #Inherit models
    _inherit='stock.lot',
    
    @api.model
    def _get_next_serial(self, company,product):
        product_tmpl_id=product.product_tmpl_id
        if product_tmpl_id.detailed_type == 'motorcycle' and product.tracking != "none":
            make = product_tmpl_id.make[:2].upper() if product_tmpl_id.make else 'DF'
            model= product_tmpl_id.model[:2].upper() if product_tmpl_id.model else 'DF'
            year= str(product_tmpl_id.year)[:-2] if product_tmpl_id.year else '00'
            battery_capacity=product_tmpl_id.battery_capacity.upper() if product_tmpl_id.battery_capacity else 'S'
            return make+model+year+battery_capacity+self.env['ir.sequence'].next_by_code('stock.lot.serial')
        else:
            return super(StockLot,self)._get_next_serial(company,product)