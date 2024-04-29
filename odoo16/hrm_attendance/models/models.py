# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ResPartner(models.Model):
#     _inherit = "res.partner"
#     anshu = fields.Char("loyalty points")


class ProfileInfo(models.Model):
    _name = 'profile_info'
    _description = 'profile_info'

    name = fields.Char(string="Name")
    designation = fields.Char(string='Designation')
    department = fields.Char(string='Department')
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='upload your profile' ,help="select image here")
    adhar = fields.Char(string='Adhar number')
    phone = fields.Char(string='Phone')
    guidance_name = fields.Char(string='Guidance Name')
    guidance_phone = fields.Char(string='Guidance phone')
    salary_inhand = fields.Float(string='Salary in hand')
    salary_gross = fields.Float(string='Salary in Gross')

    #old experience
    experience = fields.Boolean(string="Experience")
    year_n_month = fields.Char(string="Year/Months")
    company_name = fields.Char(string ="Company name")
    profile = fields.Char(string="Profile")
    salary = fields.Char(string="Salary")
    
    #skills 
    graduation = fields.Char(string="Graduation")
    skills = fields.Char(string="Skills")
    additional_skill =fields.Char(string="Additional skill")
    course = fields.Char(string="Course")
    certificates = fields.Char(string="Certificates")
    


