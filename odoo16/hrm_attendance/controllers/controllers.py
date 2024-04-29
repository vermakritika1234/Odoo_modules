# -*- coding: utf-8 -*-
# from odoo import http


# class HrmAttendance(http.Controller):
#     @http.route('/hrm_attendance/hrm_attendance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hrm_attendance/hrm_attendance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hrm_attendance.listing', {
#             'root': '/hrm_attendance/hrm_attendance',
#             'objects': http.request.env['hrm_attendance.hrm_attendance'].search([]),
#         })

#     @http.route('/hrm_attendance/hrm_attendance/objects/<model("hrm_attendance.hrm_attendance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hrm_attendance.object', {
#             'object': obj
#         })
