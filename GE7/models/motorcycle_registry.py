class MotorcycleRegistry(models.Model):
    _inherits = "product.template"
    name = fields.Char(compute="_compute_name")

    @api.depends("year", "make", "model")
    def _compute_name(self):
        for record in self:
            if record.detailed_type=="motorcycle":
                record.name = record.year+record.make+record.model

