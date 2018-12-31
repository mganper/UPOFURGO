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

class vehiculo(osv.Model):
    
    _name = 'vehiculo'
    _description = 'clase vehiculo'
 
    _columns = {
           'modelo': fields.char('Modelo', size=50),
           'matricula': fields.char('Matricula', size=128),
           'fechaAdquisicion': fields.datetime('Fecha adquisicion', required=True, autodate = True),
           'fechaProximaRevision': fields.datetime('Fecha Proxima Revision', required=True, autodate = True),
           
           'transportista_id': fields.many2many('transportista','transp_vehic_rel','dni','matricula','Transportistas'),
        }