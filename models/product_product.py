from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    ada_location_ids = fields.One2many(
        comodel_name='product.ada.location',
        inverse_name='product_id',
        string='Ubicaciones ADA',
    )
