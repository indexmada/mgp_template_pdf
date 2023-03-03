from odoo import models, fields

# LA GESTION DE BRAND #
class MyBrand(models.Model):
    _name = 'my_brand.brand'
    _description = 'My Brand'

    name = fields.Char(string='Brand Name', required=True)
    description = fields.Text(string='Description')
    logo = fields.Binary(string='Logo')

#------------FIN gestion de BRAND---------------------#



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

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    x_brand = fields.Char(string='Brand')


#--------HERITAGE DU MODELE PRODUCT TEMPLATE ICI------------------------ #
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_brand = fields.Char(string='Brand')
    x_brand_id = fields.Many2one('my_brand.brand', string='Brand')

    x_brand = fields.Many2one('my_brand.brand', string='Brand', index=True, group_expand='_group_expand_brand')

    @api.model
    def _group_expand_brand(self, brands, order):
        return self.env['my_brand.brand'].search([], order=order)

    
