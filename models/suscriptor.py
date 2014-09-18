# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la clase suscriptor
class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
    
    _columns = {
        'name': fields.char('Nombre y Apellido'),
        'identification': fields.char('Cédula', required=True),
        'address': fields.text('Dirección'),
    }
    
    _sql_constraints = [
        ('identification_uniq', 'unique(identification)', 
        u'El numero de cédula o pasaporte no se puede repetir.'),
    ]
    
suscriptor()
