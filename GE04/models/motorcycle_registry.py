from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _inherit='motorcycle.registry'
    
    # repair_ids= fields.One2many(comodel_name='repair.order',inverse_name="registry_id")
    
    def action_repair_order_tree(self):
        pass