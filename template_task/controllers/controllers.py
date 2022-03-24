# -*- coding: utf-8 -*-
# from odoo import http


# class TemplateTask(http.Controller):
#     @http.route('/template_task/template_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/template_task/template_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('template_task.listing', {
#             'root': '/template_task/template_task',
#             'objects': http.request.env['template_task.template_task'].search([]),
#         })

#     @http.route('/template_task/template_task/objects/<model("template_task.template_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('template_task.object', {
#             'object': obj
#         })
