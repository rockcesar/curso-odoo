# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime
#Tupla de los tipos de suscripcion
TIPOS = [
    ('oro', 'Plan ORO'),
    ('plata', 'Plan PLATA'),
    ('bronce', 'Plan BRONCE'),
]

#Definicion de la tabla suscripcion
class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _descripcion = 'CO Suscripcion'
    _rec_name = 'code'
    
    _columns = {
        'code': fields.char('Código de la suscripción'),
        'type': fields.selection(TIPOS, 'Tipo de suscripción'),
        'date_start': fields.date('Fecha de Inicio de suscripcion'),
        'date_end': fields.date('Fecha de Fin de suscripcion'),
        'active': fields.boolean('Active'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
    }
    
    _defaults = {
        'active': True,
        'date_start': datetime.now().strftime('%Y-%m-%d'),
        #~ 'code': lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion'),
    }
    
    def create(sef, cr, uid, values, context=None):
        if context is None:
            context={}
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
            
        return super(suscripcion, self).write(cr, uid, values, context=context)

suscripcion()
