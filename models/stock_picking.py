from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_view_products(self):
        action = super().action_view_products()
        if not action:
            return action

        context = dict(action.get("context", {}))
        pricelist_id = self.env.company.x_receipt_pricelist_id.id
        if pricelist_id:
            context["pricelist_id"] = pricelist_id

        if action.get("res_model") == "product.product":
            tree_view = self.env.ref(
                "stock_picking_product_link_pricelist.product_product_tree_view_receipt"
            )
            action["views"] = [(tree_view.id, "tree"), (False, "form")]
        elif action.get("res_model") == "product.template":
            tree_view = self.env.ref(
                "stock_picking_product_link_pricelist.product_template_tree_view_receipt"
            )
            action["views"] = [(tree_view.id, "tree"), (False, "form")]

        action["context"] = context
        return action
