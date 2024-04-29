from odoo import models, api
import logging
class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.model
    def create(self,vals):
        vals ={
            'name':"kritika verma",
            "partner_id" :43,
            # "order_line" : order_lines.id

        }
        logging.info(f"==self =========={self}===vals={vals}")

        res = super(SaleOrder,self).create(vals)

        logging.info(f"===res line 28=============={res}")
        orderlines ={
            'order_id' : res.id,
            'name' : 'Custom automatic template product',
            'product_id' :46,
            'product_uom_qty':1,
            'qty_delivered':1,
            'qty_invoiced' :1,
            'customer_lead':1,
            'price_unit':20,
            'tax_id':[(6,0,[2])],
        }

        order_lines = self.env['sale.order.line'].create(orderlines)
        logging.info(f"==order lines line 21====={res}======{order_lines}")

        if res:
            actionConfirm = res.action_confirm()
            if actionConfirm:
                delivery_vals ={
                    'name' :res.name,
                    'partner_id':res.partner_id,
                    

                }
        return res
    
    # @api.multi
    def automatic_sale_order(self):
        logging.info(f"self=7=={self}")
        vals={}
        self.create(vals)
        return True


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


