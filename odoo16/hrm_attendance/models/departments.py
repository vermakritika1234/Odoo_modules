# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hrm_Department(models.Model):
    _name = 'hrm_department'
    _description = 'hrm_department'
    
    DEPARTMENTS =[('admin','Admin'),('hr','Human Resource'),('odoo','ODOO'),('php','PHP')]
    department = fields.Selection(DEPARTMENTS,string='Add you Departments')


