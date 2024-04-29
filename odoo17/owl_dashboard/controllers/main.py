from odoo import http
from odoo.http import request
import json
import logging
class WebsiteController(http.Controller):

    @http.route(['/salesdata/'],type="http",auth='public',website="True")
    def sale_data(self, **post):
        sales_data = request.env['sale.order'].sudo().search([])
        # values = {
        #             "records": sales_data
        #     } 
        # logging.info(f"====json data line 14=======values-=={values}==json data==={type(values)}")
        # json_data = json.dumps(values)
        # response = request.make_response(json_data)
        # logging.info(f"====json data line 16==========response=={response}")
        # response.headers['Content-Type'] = 'application/json'
        return http.request.render('owl_dashboard.subjects',{
                    "subjects": ['maths','english','hindi']
            } )