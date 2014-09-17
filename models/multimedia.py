# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla contenido
class multimedia(osv.osv):
    _name = 'co.multimedia'
    _descripcion = 'CO Multimedia'
    _rec_name = 'title'
    _order = 'release_date desc'

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
    }

multimedia()
