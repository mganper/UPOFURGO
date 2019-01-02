# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class bulto(osv.Model):
    
    _name = 'bulto'
    _description = 'clase bulto'
 
    _columns = {
           'identificador': fields.char('Identificador', size=50,required=True),
           'peso': fields.float('Peso', size=128),
           'descripcion': fields.char('Descripcion', size=50),
           'medidas': fields.char('Medidas', size=13),
           
           'envio_id': fields.many2one('envio', 'Envio',required=True),
        }
    
    _sql_constraints = [ ('id_bulto', 'unique (identificador)', 'Ya existe ese id'),  ]