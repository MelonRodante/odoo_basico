# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_basico.suceso' #Nombre de la tabla
    _description = 'Tipos de datos basicos'

    name = fields.Char(string="Titulo",size=20,required=True)
    descripcion = fields.Text(string="La descripcion:")
    nivel = fields.Selection([('Alto','Alto'),('Medio','Medio'),('Bajo','Bajo')], string="Sexo:")
    data_hora = fields.Datetime(string="Data e Hora")