from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_lieu_des_travaux = fields.Char(string='Lieu des travaux')


class ResCompany(models.Model):
    _inherit = 'res.company'

    x_nif = fields.Char(string='NIF')
    x_stat = fields.Char(string='STAT')
    x_rcs = fields.Char(string='RCS')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_nif = fields.Char(string='NIF')
    x_stat = fields.Char(string='STAT')
    x_rcs = fields.Char(string='RCS')
