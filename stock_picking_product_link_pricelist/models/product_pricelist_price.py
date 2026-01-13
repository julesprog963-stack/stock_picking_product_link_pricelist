from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    x_pricelist_price = fields.Monetary(
        string="Pricelist Price",
        compute="_compute_x_pricelist_price",
        currency_field="x_pricelist_currency_id",
        store=False,
        readonly=True,
    )
    x_pricelist_currency_id = fields.Many2one(
        comodel_name="res.currency",
        compute="_compute_x_pricelist_price",
        store=False,
        readonly=True,
    )

    @api.depends_context("pricelist_id")
    def _compute_x_pricelist_price(self):
        pricelist_id = self.env.context.get("pricelist_id") or self.env.company.x_receipt_pricelist_id.id
        pricelist = self.env["product.pricelist"].browse(pricelist_id) if pricelist_id else self.env["product.pricelist"]
        currency = pricelist.currency_id if pricelist else self.env.company.currency_id
        if not pricelist:
            for product in self:
                product.x_pricelist_currency_id = product.currency_id or currency
                product.x_pricelist_price = product.list_price
            return

        prices = pricelist._get_products_price(self, 1.0)
        for product in self:
            product.x_pricelist_currency_id = currency
            product.x_pricelist_price = prices.get(product.id, 0.0)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_pricelist_price = fields.Monetary(
        string="Pricelist Price",
        compute="_compute_x_pricelist_price",
        currency_field="x_pricelist_currency_id",
        store=False,
        readonly=True,
    )
    x_pricelist_currency_id = fields.Many2one(
        comodel_name="res.currency",
        compute="_compute_x_pricelist_price",
        store=False,
        readonly=True,
    )

    @api.depends_context("pricelist_id")
    def _compute_x_pricelist_price(self):
        pricelist_id = self.env.context.get("pricelist_id") or self.env.company.x_receipt_pricelist_id.id
        pricelist = self.env["product.pricelist"].browse(pricelist_id) if pricelist_id else self.env["product.pricelist"]
        currency = pricelist.currency_id if pricelist else self.env.company.currency_id
        if not pricelist:
            for template in self:
                template.x_pricelist_currency_id = template.currency_id or currency
                template.x_pricelist_price = template.list_price
            return

        prices = pricelist._get_products_price(self, 1.0)
        for template in self:
            template.x_pricelist_currency_id = currency
            template.x_pricelist_price = prices.get(template.id, 0.0)
