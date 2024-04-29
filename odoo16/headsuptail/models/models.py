# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UserRegister(models.Model):
    _name = 'user.registration'

    name= fields.Char(string="name")
    age = fields.Integer(string='Age')
    designation = fields.Char(string="designation")
    books_record_ids = fields.One2many('books.books','books_id',string="book_books data")
    books_data_ids = fields.One2many('books.books','books_id',string="book data")