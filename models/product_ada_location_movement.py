from odoo import fields, models


class ProductAdaLocationMovement(models.Model):
    _name = 'product.ada.location.movement'
    _description = 'Bitacora de movimientos ADA (append-only)'
    # Nota de diseño: este modelo no contiene código que cree registros de movimiento
    # de forma automática (sin overrides, sin crons, sin hooks de evento).
    # La lógica de negocio que genera movimientos (confirmaciones de entradas, salidas,
    # ajustes) vive en el proyecto de operaciones externo. Este módulo solo define el
    # esquema de la bitácora y los permisos de lectura; la escritura ocurre desde fuera.
    _rec_name = 'location'

    location_entry_id = fields.Many2one(
        comodel_name='product.ada.location',
        string='Entrada de ubicacion',
        required=True,
        ondelete='restrict',
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
