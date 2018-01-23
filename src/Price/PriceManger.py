# coding=utf-8
# @File  : PriceManger.py
# @Author: PuJi
# @Date  : 2018/1/19 0019

from PriceDbDict import PriceDbDict
from Config import config
import os


class PriceManager(object):
    def __init__(self,site):
        self.site = site
        self.log = self.site.log
        self.site_address = os.path.join(config.data_dir, site.address)
        self.price_dbpath = os.path.join(self.site_address, 'price.db')
        self.prices = PriceDbDict(site)

    def loadPrices(self):
        if len(self.prices) == 0:
            self.log.debug("PriceDb not initialized, load prices from filesystem")