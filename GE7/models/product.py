import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"
    name = fields.Char(compute="_compute_name",store=True, readonly=False)

    @api.depends("year", "make", "model")
    def _compute_name(self):
        for record in self:
            print(record)
            print(record.year, record.model, record.make)
            print(type(record.year), type(record.model), type(record.make))
            if record.detailed_type == "motorcycle":
                record.name = str(record.year)+" "+str(record.make)+" "+str(record.model)

