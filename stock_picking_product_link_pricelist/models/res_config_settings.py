from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    x_receipt_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Pricelist for receipt report",
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    x_receipt_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        related="company_id.x_receipt_pricelist_id",
        string="Pricelist for receipt report",
        readonly=False,
    )
