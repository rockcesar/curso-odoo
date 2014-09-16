# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla tienda
class tienda(osv.osv):
    _name = 'co.tienda'
    _descripcion = 'CO Tienda'
    
    _columns = {
        'name': fields.char('Nombre de tienda'),
        'address': fields.text,
    }

tienda()
