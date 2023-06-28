odoo.define('website.s_odometer', function (require) {
    'use strict';

    const { ColorpickerWidget } = require('web.Colorpicker');
    const core = require('web.core');
    const publicWidget = require('web.public.widget');
    const weUtils = require('web_editor.utils');

    const qweb = core.qweb;
    const _t = core._t;
    const OdometerWidget = DynamicWidget.extend({
        selector: '.s_odometer',
        model: 'motorcycle.registry',
        /**
        *
        * @override
        */
        willStart: function () {
            this.el.dataset.filterId = 
            this.el.dataset.templateKey =
            super.willStart().then(_ => {
                let miles = 0;
                this.data.forEach(e => {
                    miles += e.current_mileage;
                });
                this.total_mileage = miles;
                this.$('#odometer-total').text(this.total_mileage);
            });
            
        },
    });
});