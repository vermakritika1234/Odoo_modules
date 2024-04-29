# -*- coding: utf-8 -*-
# from odoo import http


# class Headsuptail(http.Controller):
#     @http.route('/headsuptail/headsuptail', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/headsuptail/headsuptail/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('headsuptail.listing', {
#             'root': '/headsuptail/headsuptail',
#             'objects': http.request.env['headsuptail.headsuptail'].search([]),
#         })

#     @http.route('/headsuptail/headsuptail/objects/<model("headsuptail.headsuptail"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('headsuptail.object', {
#             'object': obj
#         })
