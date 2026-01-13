# Porting Notes - stock_picking_product_link_pricelist

- Built for Odoo 17.0 Community.
- Depends on stock_picking_product_link_port_v17 in this repo because
  stock_picking_product_link is not installable in the current environment.
- Uses product.pricelist._get_products_price for real pricelist computation.
- Adds a dedicated tree view for the picking flow via context tree_view_ref.
