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
        'code': fields.char('Código de la suscripción', help="El código se genera luego de guardar"),
        'type': fields.selection(TIPOS, 'Tipo de suscripción', required=True),
        'date_start': fields.date('Fecha de Inicio de suscripcion', required=True),
        'date_end': fields.date('Fecha de Fin de suscripcion', required=True),
        'active': fields.boolean('Active'),
        'suscriptor_id': fields.many2one(
            'co.suscriptor', 
            'Afiliado', 
            required=True),
    }
    
    _defaults = {
        'active': True,
        'date_start': datetime.now().strftime('%Y-%m-%d'),
        #~ 'code': lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion'),
    }
    
    def _check_dates(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        for s in self.browse(cr, uid, ids, context=context):
            if s.date_end <= s.date_start:
                return False
        return True
    
    _constraints = [
        (_check_dates, 'Fecha de inicio debe ser menor a fecha final',
        ['date_start', 'date_end']),
    ]
    
    def create(self, cr, uid, values, context=None):
        if context is None:
            context={}
        #~ Ejecutar una sentencia SQL
        #~ sql = ''
        #~ cr.execute(sql)
        #~ cr.fetchall()
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
            
        return super(suscripcion, self).create(cr, uid, values, context=context)

suscripcion()
