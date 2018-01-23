# coding=utf-8
# @File  : PriceCusor.py
# @Author: PuJi
# @Date  : 2018/1/22 0022

# from Db import DbCursor
#
#
# class PriceCursor(DbCursor):
#     def __init__(self, conn, db):
#         DbCursor.__init__(conn, db)

    # def needTable(self, table, cols, indexes=None, version=1):
    #     current_version = self.price_version
    #     if int(current_version) < int(version):  # Table need update or not extis
    #         self.db.log.info("Table %s outdated...version: %s need: %s, rebuilding..." % (table, current_version, version))
    #         self.createTable(table, cols)
    #         if indexes:
    #             self.createIndexes(table, indexes)
    #
    #         return True
    #     else:  # Not changed
    #         return False
