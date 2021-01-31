# -*- coding: utf-8 -*-
{
    'name': "Index Sale Days",

    'summary': """
        Rajouter le nombre de jours de location sur les devis et factures.
        """,

    'description': """
        Rajouter le nombre de jours de location sur les devis et factures.
    """,

    'author': "Index Consulting",
    'website': "https://index-mada.com/",

    'category': 'Uncategorized',
    'version': '13.0.1.0.0',

    'depends': [
        'base',
        'sale',
        'account',
    ],

    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
    ],

}
