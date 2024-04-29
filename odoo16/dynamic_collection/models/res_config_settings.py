
from odoo import models, fields, api



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_no = fields.Char(string='account')