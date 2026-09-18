{
    'name': 'Product ADA Location',
    'version': '18.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Registro de ubicaciones físicas ADA/LOGIS por variante de producto',
    'author': 'Rosa de Lima',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
