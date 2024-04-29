# from odoo import models, fields,api
# import datetime
# from datetime import datetime
# import logging
# _logger = logging.getLogger(__name__)

# class Librarian(models.Model):
#     _name = 'library.library'
#     # _inherit = ['books.books']

#     name = fields.Char(string="name")
#     section = fields.Selection([('comic','Comic'),('upsc','UPSC'),('fairy','Fairy tales')],string="section")
#     book_to_students = fields.Selection([('first','I'),('fifth','V'),('ninth','IX'),("tenth",'X')],string="class")
#     book_issue = fields.Many2one('books.books',string="book issued")
#     date_from = fields.Datetime(string="Date from")
#     date_to = fields.Datetime(string="Date to")
#     duration = fields.Char(string="duration in days")