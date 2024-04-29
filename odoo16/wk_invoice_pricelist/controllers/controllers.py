# -*- coding: utf-8 -*-
# from odoo import http


# class WkInvoicePricelist(http.Controller):
#     @http.route('/wk_invoice_pricelist/wk_invoice_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wk_invoice_pricelist/wk_invoice_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('wk_invoice_pricelist.listing', {
#             'root': '/wk_invoice_pricelist/wk_invoice_pricelist',
#             'objects': http.request.env['wk_invoice_pricelist.wk_invoice_pricelist'].search([]),
#         })

#     @http.route('/wk_invoice_pricelist/wk_invoice_pricelist/objects/<model("wk_invoice_pricelist.wk_invoice_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wk_invoice_pricelist.object', {
#             'object': obj
#         })
