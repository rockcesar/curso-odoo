# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Definicion de la tabla categoria
class categoria(osv.osv):
    _name = 'co.categoria'
    _descripcion = 'CO Categoria'
    
    _columns = {
        'name': fields.char('Nombre de categoría'),
        'description': fields.char('Descripción de categoría'),
        'parent_id': fields.many2one('co.categoria', 'Categoría Padre'),
        'child_ids': fields.one2many(
            'co.categoria', 
            'parent_id', 
            'Sub-Categorías'),
    }

categoria()
