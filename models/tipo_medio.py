# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla tipo_medio
class tipo_medio(osv.osv):
    _name = 'co.tipo.medio'
    _description = 'CO Tipo Medio'
    
    _columns = {
        'name': fields.char('Nombre'),
    }
    
tipo_medio()
