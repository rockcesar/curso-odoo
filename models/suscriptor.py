# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
    
    _columns = {
        'name': fields.char('Nombre y Apellido'),
        'identification': fields.char('Cédula'),
        'address': fields.text('Dirección'),
    }
    
suscriptor()
