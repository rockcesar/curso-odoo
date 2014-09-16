# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla lineas_stock
class lineas_stock(osv.osv):
    _name = 'co.lineas.stock'
    _descripcion = 'CO Lineas Stocks'
    
    _columns = {
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo de Medio'),
        'tienda_id': fields.many2one('co.tienda', 'Tienda'),
        'quantity': fields.integer('Cantidad'),
    }

lineas_stock()


class tienda(osv.osv):
    _inherit = 'co.tienda'
    _columns = {
        'linea_ids': fields.one2many('co.lineas.stock', 'tienda_id', 'Stock'),
    }

tienda()
