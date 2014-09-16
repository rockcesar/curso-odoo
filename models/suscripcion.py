# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

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
    
    _columns = {
        'code': fields.char('Código de la suscripción'),
        'type': fields.selection(TIPOS, 'Tipo de suscripción'),
        'date_start': fields.date('Fecha de Inicio de suscripcion'),
        'date_end': fields.date('Fecha de Fin de suscripcion'),
        'active': fields.boolean('Active'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
    }

suscripcion()
