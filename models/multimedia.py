# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla contenido
class multimedia(osv.osv):
    _name = 'co.multimedia'
    _descripcion = 'CO Multimedia'
    _rec_name = 'title'
    _order = 'release_date desc'

    def _compute_stock(self, cr, uid, ids, field_name, arg, congtext):
        stock_obj = self.pool.get('co.lineas.stock')
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = {}
        for i in ids:
            lineas_ids = stock_obj.search(cr, uid, [
                ('multimedia_id', '=', i), ])
            lineas_brw = stock_obj.browse(cr, uid, lineas_ids)
            
            #Devuelve la suma de la lista generada por 
            #'l.quantity for l in lineas_brw'
            res[i] = sum([l.quantity for l in lineas_brw])
            
        #Devuelve el resultado
        return res

    _columns = {
        'title': fields.char('Título', required=True),
        'release_date': fields.date('Fecha de publicación'),
        'code': fields.char('Código de la película'),
        'categoria_id': fields.many2one('co.categoria', 'Categoría'),
        'medio_ids': fields.many2many(
            'co.tipo.medio',
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id'),
        'stock': fields.function(_compute_stock, type='integer'),
    }

multimedia()
