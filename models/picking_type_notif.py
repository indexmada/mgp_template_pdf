from odoo import models, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        if self.picking_type_id:
            message = _('MERCI !')
            self.env['res.message'].create({
                'message_type': 'notification',
                'notification_type': 'success',
                'text': message,
                'sticky': False
            })
        return super(PurchaseOrder, self).button_confirm()
