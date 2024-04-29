# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class odoo_learning(models.Model):
    _name = 'odoo_learning.odoo_learning'
    _description = 'odoo_learning.odoo_learning'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    first = fields.Many2one(string="First")
    @api.depends('value')
    def _value_pc(self):
        for record in self:

            record.value2 = float(record.value) / 100



class Employee(models.Model):
    _name = 'employee.employee'
    name = fields.Char(string='Employee name')
    age = fields.Char(string='Employee age')

    @api.model
    def create(self,vals):
        _logger.info('call ing fucntion----')
        vals={'name':'vipul kumar','age':20}
        key ={
            'emp_name': vals['name']
        }
        self.env['product.template'].create(key)
        return super(Employee,self).create(vals)
    
    # @api.model
    def write(self,vals):
        _logger.info("inside write method------:")
        vals ={'age': 34}
        key = {'id':57,'emp_name': 'Harshita'}
        self.env['product.template'].write(key)
        return super(Employee,self).write(vals)

class ProductTemplate(models.Model):
    _inherit = "product.template"
    emp_name = fields.Char(string='Employee name')

    # @api.model
    def create(self,vals):
        # _logger.info('if it calls to create-------:%r',vals)
        # _logger.info('if it calls to create-------:%r',vals[0].get('emp_name'))

        vals ={
            'name': 'krutika a',
            'detailed_type' : 'service',
            'invoice_policy':'order',
            'categ_id':8,
            'emp_name' : 'sonia'

        }
        return super(ProductTemplate,self).create(vals)
    

    def write(self,vals):
        _logger.info("inside the write method --------71:%r",vals)
        try: 
            if vals:
                _logger.info("if vals-------:%r",vals)
                return super().write(vals)
        except Exception as e:
            _logger.info('print the error------:%r',e)


 