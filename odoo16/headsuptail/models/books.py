from odoo import models,fields,api

class Books(models.Model):
    _name ="books.books"

    books_id = fields.Many2one('user.registration',string="Books id")
    code = fields.Integer('Book code')
    name = fields.Char("Book name")
