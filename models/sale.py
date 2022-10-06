# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError
import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for orden in self:
            if self.env.user.has_group('prime.grupo_descuento_maximo_admin'):
                return super(SaleOrder, self).action_confirm()
            else:
                autorizacion_descuento = []
                if orden.order_line:
                    for linea in orden.order_line:
                        if linea.discount > linea.product_id.descuento_maximo:
                            autorizacion_descuento.append(' Nombre producto: ' + str(linea.product_id.name) + ' ,límite máximo: '+str(linea.product_id.descuento_maximo) + "% ")
                if len(autorizacion_descuento) == 0:
                    return super(SaleOrder, self).action_confirm()
                else:
                    raise ValidationError(_('No tiene permiso para validar la orden por sobrepasar limite de descuentos' + str(autorizacion_descuento)))
