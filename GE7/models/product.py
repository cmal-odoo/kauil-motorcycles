from odoo import api, fields, models;
class ProductTemplate(models.Model):
    _inherit = "product.template"
    name = fields.Char(compute="_compute_name", store=True, readonly=False)

    @api.depends("year", "make", "model")
    def _compute_name(self):
        for record in self:
            if record.detailed_type=="motorcycle":
                record.name = str(record.year)+" "+str(record.make)+" "+str(record.model)

