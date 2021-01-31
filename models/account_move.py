# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    days_count = fields.Float(string="Nbr de jours", default=1)

    def _get_price_total_and_subtotal(self, price_unit=None, quantity=None, discount=None,
                                      currency=None, product=None, partner=None, taxes=None, move_type=None):
        """Changes : Consider days_count in quantity parameter."""
        self.ensure_one()
        return self._get_price_total_and_subtotal_model(
            price_unit=price_unit or self.price_unit,
            quantity=quantity and quantity * self.days_count or self.quantity * self.days_count,
            discount=discount or self.discount,
            currency=currency or self.currency_id,
            product=product or self.product_id,
            partner=partner or self.partner_id,
            taxes=taxes or self.tax_ids,
            move_type=move_type or self.move_id.type,
        )

    @api.onchange('quantity', 'discount', 'price_unit', 'tax_ids', 'days_count')
    def _onchange_price_subtotal(self):
        return super(AccountMoveLine, self)._onchange_price_subtotal()
