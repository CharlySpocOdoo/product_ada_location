from odoo import fields, models


class ProductAdaLocation(models.Model):
    _name = 'product.ada.location'
    _description = 'Ubicacion fisica ADA de variante de producto'
    _rec_name = 'location'
    _order = 'date desc'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Producto',
        required=True,
    )
    location = fields.Char(
        string='Ubicacion',
        required=True,
    )
    quantity = fields.Float(
        string='Cantidad',
        required=True,
    )
    date = fields.Date(
        string='Fecha',
        required=True,
        default=fields.Date.today,
    )
