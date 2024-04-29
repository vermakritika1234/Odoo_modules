# -*- coding: utf-8 -*-
# from odoo import http


# class OdooLearning(http.Controller):
#     @http.route('/odoo_learning/odoo_learning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_learning/odoo_learning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_learning.listing', {
#             'root': '/odoo_learning/odoo_learning',
#             'objects': http.request.env['odoo_learning.odoo_learning'].search([]),
#         })

#     @http.route('/odoo_learning/odoo_learning/objects/<model("odoo_learning.odoo_learning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_learning.object', {
#             'object': obj
#         })
