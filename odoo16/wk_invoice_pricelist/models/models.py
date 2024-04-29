# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    pricelist_id = fields.Many2one("product.pricelist", string="Pricelist")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self,vals):
        _logger.info('print the method when creae line 15------------------%r',vals)

        _logger.info('print the method when creae line 15------------------%r',self)

        return super(SaleOrder,self).create(vals)
    
    def write(self,vals):
        _logger.info("print hte vals line 24--------------------%r",vals)
        res = super(SaleOrder,self).write(vals)
        return res
