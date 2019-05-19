#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class Trade:

    def __init__(self, kite):
        self._k = kite
        self._b = kite._b

    def positions(self):
        return self._k.request('GET', '/portfolio/positions')

    def orders(self):
        return self._k.request('GET', '/orders')

    def place_order(self, tradingsymbol, exchange, transaction_type, quantity, variety, type, product, validity):
        order = {
            'tradingsymbol': tradingsymbol,
            'exchange': exchange,
            'transaction_type': transaction_type,
            'order_type': type,
            'quantity': quantity,
            'product': product,
            'validity': validity
        }
