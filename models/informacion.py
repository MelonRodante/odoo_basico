# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion' #Nombre de la tabla
    _description = 'Tipos de datos basicos'

    name = fields.Char(string="Titulo",size=20,required=True)
    descripcion = fields.Text(string="La descripcion:")
    autorizado = fields.Boolean(string="¿Esta autorizado?",default=True)

    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")

    alto_en_cms = fields.Integer(string="Alto en Cms.")
    ancho_en_cms = fields.Integer(string="Ancho en Cms.")
    longo_en_cms = fields.Integer(string="Longo en Cms.")

    volume = fields.Float(compute="_volume",store=True)

    @api.depends('alto_en_cms', 'ancho_en_cms', 'longo_en_cms')
    def _volume(self):
        for registro in self:
            registro.volume = float(registro.alto_en_cms) * float(registro.ancho_en_cms) * float(registro.longo_en_cms)


    peso = fields.Float(string="Peso:",digits=(6,2),default=2.7)


    densidad = fields.Float(compute="_densidad",store=True)

    @api.depends('peso', 'volume')
    def _densidad(self):
        for registro in self:
            if registro.volume != 0:
                registro.densidad = (float(registro.peso) / float(registro.volume)) * 100
            else:
                registro.densidad = 0