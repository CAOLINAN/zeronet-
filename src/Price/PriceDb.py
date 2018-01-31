# coding=utf-8
# @File  : PriceDb.py
# @Author: PuJi
# @Date  : 2018/1/19 0019
from Config import config
from Db import Db
from Debug import Debug
import os
import time
import logging

class Price(object):

    def __init__(self, path, address):
        self.path = path
        self.address = address
        self.relpath = None
        self.name = None
        self.size_files_optional = None
        self.type = None
        self.size = None
        self.size_files = None
        self.modify = None
        self.priceID = None
        self.price = 0

    def load(self):
        self.relpath = self.getRelpath()
        self.name = self.getName()
        self.type = self.getType()
        self.size = self.getSize()
        self.modify = time.time()

    def reload(self):
        # 重新加载大小和修改时间
        self.size = self.getSize()
        self.modify = time.time()

    def getRelpath(self):
        if os.path.isfile(self.path):
            data_address = os.path.join(config.data_dir, self.address)
            return os.path.relpath(self.path, data_address)
        else:
            return None

    def getName(self):
        if os.path.isfile(self.path):
            return os.path.split(self.relpath)[-1]
        else:
            return None

    def getType(self):
        if os.path.isfile(self.path) and '.' in self.path:
            return self.relpath.split('.')[-1]
        else:
            return None

    # return size of files in kb
    def getSize(self):
        if os.path.isfile(self.path):
            self.size = os.path.getsize(self.path)


class PriceDb(Db):

    def __init__(self, dbpath, address):
        Db.__init__(self, {"db_name": "PriceDb", "tables": {}}, dbpath)
        self.dbpath = dbpath
        self.address = address
        self.log = logging.getLogger("Price:%s" % self.address)
        self.site_path = os.path.join(config.data_dir, self.address)
        self.foreign_keys = True
        try:
            self.schema = self.getSchema()
            self.checkTables() # 创建数据表
        except Exception, err:
            self.log.error("Error loading price.db: %s, rebuilding..." % Debug.formatException(err))
            self.close()
            os.unlink(self.dbpath)  # Remove and try again
            self.schema = self.getSchema()
            self.checkTables()
        self.prices = {} # 一条价格记录为一个price，格式为{"relpath"：price}

    def getSchema(self):
        schema = {}
        schema["db_name"] = "PriceDb"
        schema["version"] = 1
        schema["tables"] = {}

        schema["tables"]["price"] = {
            "cols": [
                ["price_id", "INTEGER PRIMARY KEY AUTOINCREMENT"],# 设置priceID为自增，不考虑设置ID值
                ["rel_path", "TEXT UNIQUE NOT NULL"],
                ["name","TEXT"],
                ["size", "INTEGER"],
                ["price", "REAL"],
                ["size_files", "INTEGER"],
                ["size_files_optional", "INTEGER"],
                ["file_type", "TEXT"],
                ["modified", "INTEGER"]
            ],
            "indexes": [
                "CREATE UNIQUE INDEX price_key ON price (rel_path)",
                "CREATE INDEX price_modified ON price (modified)"
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

    def setPrice(self, relpath, price):
        if relpath in self.prices.keys():
            temp_price = self.prices.get(relpath)
        else:
            self.log.warning("Error get %s from self.prices" % (relpath))
            path = os.path.join(self.site_path, relpath)
            temp_price = Price(path, self.address)
            temp_price.load()
        temp_price.price = price
        try:
            self.insertOrUpdate("price", {
                "name": temp_price.name,
                "relpath": temp_price.relpath,
                "price": temp_price.price,
                "size": temp_price.size,
                "file_type": temp_price.type,
                "size_files_optional": temp_price.size_files_optional,
                "size_files": temp_price.size_files,
                "modified": int(temp_price.modify)

            }, {
                 "rel_path": price.rel_path
                 })
            self.prices[relpath] = temp_price
            return True
        except:
            self.log.error("Error set {}'s price".format(os.path.join(self.address, relpath)))
            return False

    def deletePrice(self, relpath):
        if relpath in self.prices.keys():
            self.prices.pop(relpath)
            self.log.info("Delete %s from self.prices success" % (relpath))
        else:
            # self.log
            self.log.warning("There is not %s in self.prices success" % (relpath))
        if self.execute("DELETE FROM price WHERE ?", {"rel_path": relpath}):
            self.log.info("Delete %s from self.prices success" % (relpath))
            return True
        else:
            self.log.error("Delete %s from self.prices faild!" % (relpath))
            return False

    def loadPrices(self):
        for row in self.execute("SELECT * FROM price"):
            # self.prices[row["relpath"]] = {
            #     "name":row["name"],
            #     "size": row["size",
            #     "size_files": row["size_files"],
            #     "size_files_optional": row["size_files_optional"],
            #     "file_type": row["file_type"],
            #     "modified": row["modified"]
            # }
            path = os.path.join(self.site_path, row["relpath"])
            self.prices[row["relpath"]] = Price(path, self.address)

            self.prices[row["relpath"]].priceID = row["price_id"]
            self.prices[row["relpath"]].relpath = row["relpath"]
            self.prices[row["relpath"]].name = row["name"]
            self.prices[row["relpath"]].size = row["size"]
            self.prices[row["relpath"]].price = row["price"]
            self.prices[row["relpath"]].size_files = row["size_files"]
            self.prices[row["relpath"]].size_files_optional = row["size_files_optional"]
            self.prices[row["relpath"]].type = row["file_type"]
            self.prices[row["relpath"]].modified = row["modified"]

    def getSetting(self, relpath):
        if relpath in self.prices.keys():
            return self.prices.get(relpath)
        else:
            res = self.execute(
                "SELECT * FROM price WHERE ?",
                {"rel_path": relpath}
            )
            row = res.fetchone()  # 获取结果集中的下一行
            if row:
                return row
            else:
                return None

price_dbs = {}

# 检查数据库文件是否存在，否则创建数据库
def getPriceDb(address=config.homepage):

    address_dir = os.path.join(config.data_dir, address)
    path = os.path.join(address_dir, 'price.db')

    if address not in price_dbs:
        price_dbs[address] = PriceDb(path, address)
    return price_dbs[address]

getPriceDb()


