# -*- coding: utf-8 -*-
{
    'name': 'mgp_template_pdf',
    'version': '13.0.1.0',
    'summary': 'Custom PDF report template for Quotations',
    'description': 'Custom PDF report template for Quotations in Odoo 13',
    'category': 'Sales',
    'author': 'Index',
    'depends': ['sale_management'],
    'data': [
        #'reports/sale_report_template.xml',
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/res_company.xml',
        'views/res_partner_views.xml',
        'views/product_view.xml',
        'views/brand.xml',
        'views/menu.xml',
        #'views/purchase_views.xml',
        #'static/src/js/purchase.js',
    ],
    'installable': True,
    'auto_install': False,
}
