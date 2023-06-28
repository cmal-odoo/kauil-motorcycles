from odoo import models, fields, api
from math import radians, cos, sin, asin, sqrt


class Location:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def haversine(self, other):

        self.long, self.lat, other.long, other.lat = map(radians, [self.long, self.lat, other.long, other.lat])

        diff_long = self.long - other.long
        diff_lat = self.lat - other.lat
        a = sin(diff_lat/2)**2 + cos(self.lat) * cos(other.lat) * sin(diff_long/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    def __str__(self):
        return f'{self.lat} {self.long}'


BUF_WAREHOUSE = Location(78.8784, 42.8864)
SF_WAREHOUSE = Location(122.4194, 37.7749)

'''
1 manufacturing plant
2 quality plant
3 BU
4 SF
'''


class SaleOrder(models.Model):
    _inherit = "sale.order"

    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Warehouse', required=True,
        compute='_compute_warehouse_id', store=True, readonly=False, precompute=True, default=1,
        states={'sale': [('readonly', True)], 'done': [
            ('readonly', True)], 'cancel': [('readonly', False)]},
        check_company=True)

    @api.depends('partner_id')
    def _compute_warehouse_id(self):
        for order in self:
            # longitude and latitude of the shipping location
            delivery_address_location = Location(order.partner_shipping_id.partner_longitude, order.partner_shipping_id.partner_latitude)
            distance_from_sf = delivery_address_location.haversine(SF_WAREHOUSE)
            distance_from_buf = delivery_address_location.haversine(BUF_WAREHOUSE)
            diff = distance_from_sf - distance_from_buf
            order.warehouse_id = 3 if diff > 0 else 4
