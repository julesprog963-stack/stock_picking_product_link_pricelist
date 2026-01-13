# Release Notes - stock_picking_product_link_pricelist 17.0.1.0.1

## Functional flow
- Receipt done -> open "Products" smart button -> list shows cost, list price, and pricelist price.
- Export uses the standard Odoo list export.
- Ensures a single "Products" smart button is shown even if duplicate views exist.
- Uses a dedicated receipt tree view to avoid affecting global product lists.
- Pricelist price falls back to list_price when no pricelist is configured.

## Configuration
- Settings -> Companies -> Pricelist for receipt report (company specific).

## Core validation evidence
- Base action and res_model:
  - custom_addons/stock_picking_product_link_port_v17/models/stock_picking.py (action_view_products)
- Base picking view inheritance:
  - custom_addons/stock_picking_product_link_port_v17/views/stock_picking_views.xml
- Product list tree views used:
  - odoo_core/addons/product/views/product_views.xml (product.product tree view)
  - odoo_core/addons/product/views/product_template_views.xml (product.template tree view)
- Pricelist price engine:
  - odoo_core/addons/product/models/product_pricelist.py (_get_products_price, _compute_price_rule)

## Installation / Upgrade
- docker exec odoo17-app odoo -d dev_arsenio_odoo -u stock_picking_product_link_pricelist --stop-after-init

## Packaging ZIP
- Create a clean ZIP (no __pycache__) under custom_addons/_dist:
  - stock_picking_product_link_pricelist-17.0.1.0.0.zip

## Checklist
- [ ] Settings -> Companies -> set "Pricelist for receipt report".
- [ ] Validate a receipt, click "Products".
- [ ] Columns visible: Cost (standard_price), Sales Price (list_price), Pricelist Price.
- [ ] Change list_price (product_auto_sale_price), reopen list, pricelist price updates.
- [ ] Export to CSV/XLSX from list view and confirm columns.
- [ ] No errors if pricelist is not configured (prices show 0).
