from odoo import models, fields,api
import datetime
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class students(models.Model):
    _name = 'students.students'
    # _inherit = ['books.books']

    name = fields.Char(string="name")
    class_name = fields.Selection([('first','I'),('fifth','V'),('ninth','IX'),("tenth",'X')],string="class")
    book_issue = fields.Many2one('books.books',string="book issued")
    date_from = fields.Datetime(string="Date from",default=datetime.now())
    date_to = fields.Datetime(string="Date to")
    SELECTION=[('booked','Booked'),('available','Available now')]
    duration = fields.Selection(SELECTION,string="duration in days")


    def calculate_duration(self):
        objs = self.env['students.students'].search([('date_to','!=',False)])
        current_date = datetime.now()
        for rec in objs:
            if current_date > rec.date_to:
                rec.duration = "available"
            else:
                rec.duration ='booked'
            