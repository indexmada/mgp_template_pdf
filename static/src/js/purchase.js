odoo.define('mgp_template_pdf.popup_on_save', function (require) {
    'use strict';

    var FormController = require('web.FormController');
    var session = require('web.session');
    var Dialog = require('web.Dialog');

    FormController.include({
        _onSave: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                var message = 'MERCI';
                var options = {
                    title: 'Message',
                    size: 'medium',
                };
                Dialog.alert(self, message, options);
            });
        },
    });

});
