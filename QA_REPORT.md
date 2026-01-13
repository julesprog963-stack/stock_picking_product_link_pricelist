# QA Report - stock_picking_product_link_pricelist

## Versioning
- Previous version: 17.0.1.0.0
- New version: 17.0.1.0.1

## Upgrade result
- Command:
  docker exec odoo17-app odoo -d dev_arsenio_odoo -u stock_picking_product_link_pricelist --stop-after-init
- Result: OK (registry loaded)
- Relevant log lines:
  - Loading module stock_picking_product_link_pricelist
  - Module stock_picking_product_link_pricelist loaded

## Findings
### CRITICAL
- None.

### HIGH
- None.

### MEDIUM
- Dependency alignment: the environment has `stock_picking_product_link` not installable, so the addon depends on `stock_picking_product_link_port_v17` to keep upgrades stable. If you plan to standardize on `stock_picking_product_link`, you must make that module installable and update the dependency.

### LOW
- None.

## Core validation evidence (Odoo 17)
- Base picking form view: `odoo_core/addons/stock/views/stock_picking_views.xml` (inherit target: `stock.view_picking_form`).
- Base action method: `custom_addons/stock_picking_product_link_port_v17/models/stock_picking.py` (`action_view_products`).
- Pricelist engine: `odoo_core/addons/product/models/product_pricelist.py` (`_get_products_price`, `_compute_price_rule`).
- Pricelist item base pricing fallback: `odoo_core/addons/product/models/product_pricelist_item.py` (`_compute_price`).
- Settings base view: `odoo_addons_core/addons/base_setup/views/res_config_settings_views.xml` (`base_setup.res_config_settings_view_form`).

## UI checklist
- [ ] Ajustes -> Ajustes generales -> “Pricelist for receipt report” configurada.
- [ ] Inventario -> Recepciones -> DONE -> botón Productos.
- [ ] Columnas visibles: estándar (Producto), Costo (standard_price), Precio venta (list_price), Precio con lista.
- [ ] Producto sin regla específica: precio con lista = list_price.
- [ ] Export estándar incluye las columnas.

## Code quality checks
- Computed field non-stored and read-only: OK (`x_pricelist_price`, store=False).
- Uses real pricelist engine: OK (`product.pricelist._get_products_price`).
- Fallback when no pricelist configured: uses list_price (no 0.0).
- No writes to price fields: OK.
- Views limited to picking flow: OK (dedicated tree views + action override).

## Cleanup
- No __pycache__/pyc/pyo/DS_Store found under the module folder.
