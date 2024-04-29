# -*- coding: utf-8 -*-
# from odoo import http


# class DynamicCollection(http.Controller):
#     @http.route('/dynamic_collection/dynamic_collection', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dynamic_collection/dynamic_collection/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dynamic_collection.listing', {
#             'root': '/dynamic_collection/dynamic_collection',
#             'objects': http.request.env['dynamic_collection.dynamic_collection'].search([]),
#         })

#     @http.route('/dynamic_collection/dynamic_collection/objects/<model("dynamic_collection.dynamic_collection"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dynamic_collection.object', {
#             'object': obj
#         })
