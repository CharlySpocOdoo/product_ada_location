from odoo import fields, models


class ProductAdaLocationMovement(models.Model):
    _name = 'product.ada.location.movement'
    _description = 'Bitacora de movimientos ADA (append-only)'
    _rec_name = 'location'

    location_entry_id = fields.Many2one(
        comodel_name='product.ada.location',
        string='Entrada de ubicacion',
        required=True,
    )
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
    date = fields.Datetime(
        string='Fecha',
        required=True,
        default=fields.Datetime.now,
    )
    movement_type = fields.Selection(
        selection=[
            ('entrada_proveedor', 'Entrada proveedor'),
            ('entrada_inicial', 'Entrada inicial'),
            ('salida_traspaso', 'Salida traspaso'),
            ('ajuste', 'Ajuste'),
        ],
        string='Tipo de movimiento',
    )
    picking_id = fields.Many2one(
        comodel_name='stock.picking',
        string='Traspaso / Recepcion',
    )
