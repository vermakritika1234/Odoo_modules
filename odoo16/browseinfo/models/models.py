# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    show_warehouse = fields.Boolean(string='Show Warehouse')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    
    @api.model
    def create(self, vals):
        if vals.get('show_warehouse'):
            warehouse_id = self.env['stock.warehouse'].browse(vals.get('warehouse_id'))
            vals['warehouse_id'] = warehouse_id.id
        return super(SaleOrderLine, self).create(vals)
    

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line.filtered(lambda l: l.show_warehouse and l.warehouse_id and l.product_id):
                moves = self.env['stock.move'].search([('product_id', '=', line.product_id.id)])
                move_lines = []
                for move in moves:
                    move_lines.append((0, 0, {
                        'name': move.name,
                        'product_id': move.product_id.id,
                        'product_uom_qty': move.product_uom_qty,
                        'product_uom': move.product_uom.id,
                        'location_id': move.location_id.id,
                        'location_dest_id': move.location_dest_id.id,
                    }))

                picking_vals = { 
                    'picking_type_id':  self.env['stock.picking.type'].search([('name', '=', order.picking_policy)], limit=1).id,
                    'location_id': order.partner_shipping_id.property_stock_customer.id,
                    'location_dest_id': line.warehouse_id.lot_stock_id.id,
                    'move_line_ids': move_lines,
                    'operation_type':'outgoing',
                }
                if all(picking_vals.values()):
                        order.picking_ids += self.env['stock.picking'].create(picking_vals)
                else:
                    logging.warning('Mandatory fields are not set for picking creation.')
            else:
                logging.warning('Picking type not found for order: %s', order.name)
        return res






sale_order= 219
customer_name = sale_order.partner_id
order_name = sale_order.name
for i in sale_order.order_line:
    product_name =i.product_id

