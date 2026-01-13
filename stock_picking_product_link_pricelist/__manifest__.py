{
    "name": "Stock Picking Product Link Pricelist",
    "version": "17.0.1.0.1",
    "summary": "Show cost, list price, and pricelist price in received products list",
    "images": ["static/description/icon.png"],
    "author": "Local",
    "license": "AGPL-3",
    "depends": ["stock_picking_product_link_port_v17", "product"],
    "data": [
        "views/product_tree_inherit.xml",
        "views/stock_picking_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
