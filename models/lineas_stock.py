# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla lineas_stock
class lineas_stock(osv.osv):
    _name = 'co.lineas.stock'
    _descripcion = 'CO Lineas Stocks'
    _rec_name = 'quantity'
    
    _columns = {
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia', required=True),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo de Medio', required=True),
        'tienda_id': fields.many2one('co.tienda', 'Tienda'),
        'quantity': fields.integer('Cantidad', required=True),
    }
    
    def onchange_medio_id(self, cr, uid, ids, medio_id):
        return {
            'value': {
                'multimedia_id': False,
                'quantity': 0,
            }
        }
        
    def _check_qty(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        for s in self.browse(cr, uid, ids, context=context):
            if s.quantity < 0:
                return False
        return True
    
    _constraints = [
        (_check_qty, 'La cantidad no puede ser negativa.', ['quantity'])
    ]
    
    _sql_constraints = [
        ('stock_media_tienda', 
         'unique(medio_id, tienda_id, multimedia_id)', 
         u'Ya está definido el stock, actualice.')
    ]
    
lineas_stock()


class tienda(osv.osv):
    _inherit = 'co.tienda'
    _columns = {
        'linea_ids': fields.one2many(
            'co.lineas.stock', 
            'tienda_id', 
            'Stock'),
    }
    
    def unlink(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        
        for t in self.browse(cr, uid, ids, context=context):
            linea_ids = [l.id for l in t.linea_ids]
            if self.pool.get('co.lineas.stock').unlink(cr, uid, linea_ids):
                if super(tienda, self).unlink(cr, uid, t.id, context=context):
                    continue
                return False
        return True

tienda()
