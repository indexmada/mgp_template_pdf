# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    days_count = fields.Float(string="Nbr de jours", default=1)

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'days_count')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        Changes : Consider days_count
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            qty = line.product_uom_qty * line.days_count
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    def _prepare_invoice_line(self):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['days_count'] = self.days_count
        return res
