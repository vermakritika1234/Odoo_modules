# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dynamic_collection(models.Model):
    _name = 'dynamic_collection.dynamic_collection'
    _description = 'dynamic_collection.dynamic_collection'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_no = fields.Char(string='account')