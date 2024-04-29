from odoo import fields,models,api
import logging
_logger = logging.getLogger(__name__)


class OpenWizard(models.TransientModel):
    _name ="open.wizard"

    department = fields.Char(string="department")
    books_issued = fields.Integer(string="book issued")


    def action_to_create_wizard(self):
        _logger.info("calling wizard button------------------------------------------")
        return True