# coding=utf-8
# @File  : PriceDb.py
# @Author: PuJi
# @Date  : 2018/1/19 0019
from Config import config
from Db import Db
from Debug import Debug
import os
import time

class PriceDb(Db):
    def __init__(self, path):
        Db.__init__(self, {"db_name": "PriceDb", "tables": {}}, path)
        self.foreign_keys = True
        try:
            self.schema = self.getSchema()
            print(getattr(self))
            self.checkTables() # 创建数据表
        except Exception, err:
            self.log.error("Error loading price.db: %s, rebuilding..." % Debug.formatException(err))
            self.close()
            os.unlink(self.dbpath)  # Remove and try again
            self.schema = self.getSchema()
            self.checkTables()
        self.price_ids = {}
        self.prices = {}

    def getSchema(self):
        schema = {}
        schema["db_name"] = "PriceDb"
        schema["version"] = 1
        schema["tables"] = {}

        schema["tables"]["price"] = {
            "cols": [
                ["price_id", "INTEGER PRIMARY KEY UNIQUE NOT NULL"],
                ["rel_path", "TEXT UNIQUE NOT NULL"],
                ["name","TEXT"],
                ["size", "INTEGER"],
                ["size_files", "INTEGER"],
                ["size_files_optional", "INTEGER"],
                ["file_type", "TEXT"],
                ["modified", "INTEGER"]
            ],
            "indexes": [
                "CREATE UNIQUE INDEX price_key ON price (rel_path)",
                "CREATE INDEX content_modified ON content (modified)"
            ],
            "schema_changed": 1
        }

        return schema

    def checkTables(self):
        s = time.time()
        changed_tables = []
        cur = self.getCursor()

        cur.execute("BEGIN")

        # Check internal tables
        # Check keyvalue table
        changed = cur.needTable("keyvalue", [
            ["keyvalue_id", "INTEGER PRIMARY KEY AUTOINCREMENT"],
            ["key", "TEXT"],
            ["value", "INTEGER"],
            ["json_id", "INTEGER"],
        ], [
            "CREATE UNIQUE INDEX key_id ON keyvalue(json_id, key)"
        ], version=self.schema["version"])
        if changed:
            changed_tables.append("keyvalue")

        # Check schema tables
        for table_name, table_settings in self.schema["tables"].items():
            changed = cur.needTable(
                table_name, table_settings["cols"],
                table_settings["indexes"], version=table_settings["schema_changed"]
            )
            if changed:
                changed_tables.append(table_name)

        cur.execute("COMMIT")
        self.log.debug("Db check done in %.3fs, changed tables: %s" % (time.time() - s, changed_tables))
        if changed_tables:
            self.db_keyvalues = {}  # Refresh table version cache

        return changed_tables

    # def getCursor(self):
    #     if not self.conn:
    #         self.connect()
    #     return PriceCursor(self.conn, self)


price_dbs = {}

# 检查数据库文件是否存在，否则创建数据库
def getPriceDb(address=None):

    if address:
        address_dir = os.path.join(config.data_dir, address)
        path = os.path.join(address_dir, 'price.db')
    else:
        # path = os.path.join(config.data_dir, 'price.db')
        return False
    if address not in price_dbs:
        price_dbs[address] = PriceDb(path)
        path = os.path.join("E:\ZeroNet-master", path)
        print("CLN_path :   ",path)
        print("address:  ", address)
    return price_dbs[address]

getPriceDb()
