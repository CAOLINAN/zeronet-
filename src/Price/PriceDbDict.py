# coding=utf-8
# @File  : Price.py
# @Author: PuJi
# @Date  : 2018/1/22 0022
import PriceDb

import time
import os

class PriceDbDict(dict):
    def __init__(self, site):
        self.site = site
        self.log = self.site.log
        self.db = PriceDb.getPriceDb(self.site.ad)
        self.db_id = self.db.needSite(site)
        self.num_loaded = 0
        super(PriceDbDict, self).__init__(self.db.loadDbDict(site))  # Load keys from database
        self.log.debug("PriceDb init: %.3fs, found files: %s, sites: %s" % (time.time() - s, len(self), len(self.db.site_ids)))
