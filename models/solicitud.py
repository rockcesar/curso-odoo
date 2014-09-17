# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla solicitud
class solicitud(osv.osv):
    _name = 'co.solicitud'
    _descripcion = 'CO Solicitud'
    _rec_name = 'code'
    
    _columns = {
        'code': fields.char('Código'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo de Medio'),
        'tienda_id': fields.many2one('co.tienda', 'Tienda'),
        'requested_date': fields.date('Fecha solicitada'),
        'qty_days': fields.integer('Duración (en días)'),
    }

solicitud()
