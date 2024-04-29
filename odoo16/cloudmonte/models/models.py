from odoo import models, fields, api


class CustomModel(models.Model):
    _name = 'custom.model'
    # _inherit = 'sale.order'
    # _inherits ={'sale.order':'sale_partner_id'}
    # sale_partner_id = fields.Many2one('sale.order',string='partner custom',required=True,ondelete='cascade')
    name = fields.Char(string="Name of the model")
    age = fields.Char(string='age')
  
    def name_get(self):
        result = []
        for custom in self:
            name = f"{custom.name} ({custom.age}) - {custom.name}"
            result.append((custom.id, name))
        return result

# class CustomSaleOrder(models.Model):
#     _inherit = 'sale.order'
    # _inherits ={'sale.order':'partner_id'}
    # partner_id = fields.Many2one('sale.order',string="partner cycle",ondelete='cascade')
    # cycle_id = fields.Char("cycel ofc",compute="_compute_cycle_data")


    def _compute_cycle_data(self):
        for i in self:
            if i.partner_id:
                i.cycle_id = i.partner_id.name
            else:
                i.cycle_id = 'no name is there'
    # days_expiration = fields.Integer(string='Days Expiration', compunte='_compute_days_expiration')
    # @api.depends('validity_date')
    # def _compute_days_expiration(self):
    #     for order in self:
    #         if order.validity_date:
    #             current_date = fields.Date.today()
    #             expiration_date = fields.Date.from_string(order.validity_date)
    #             order.days_expiration = (expiration_date - current_date).days
    #         else:
    #             order.days_expiration = 0

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'



class ResPartner(models.Model):
    _inherit = 'res.partner'
    loyalty_points = fields.Integer(string='Loyalty Points')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    expected_date = fields.Date(string='Expected Date')
