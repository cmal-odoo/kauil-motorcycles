from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):

        res = super().button_validate()
        for move in self.move_line_ids:
            if move.picking_id.location_dest_id == self.env.ref('stock.stock_location_customers'):
                if move.product_id.detailed_type == 'motorcycle':
                    if not self.env['motorcycle.registry'].search([('vin', '=', move.lot_id.name)]):
                        self.env['motorcycle.registry'].create({
                        # Add motorcycle info here
                            'vin' :  move.lot_id.name,
                            'related_order': self.sale_id.id,
                            'lot_ids': [(6, 0, [move.lot_id.id])],
                        })

        return res

