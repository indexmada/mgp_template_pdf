from odoo import api, fields, models


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
    
    x_brand = fields.Char(string='Marque')


#--------HERITAGE DU MODELE PRODUCT TEMPLATE ICI------------------------ #
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    #x_brand = fields.Many2one('my_brand.brand', string='Marque')
    x_brand_id = fields.Many2one('my_brand.brand', string='Marque', index=True, group_expand='_group_expand_brand')

    

    @api.model
    def _group_expand_brand(self, brands, order):
        return self.env['my_brand.brand'].search([], order=order)


    def _search_x_brand_id(self, operator, value):
        product_ids = self.search([('x_brand_id', operator, value)]).ids
        return [('id', 'in', product_ids)]
