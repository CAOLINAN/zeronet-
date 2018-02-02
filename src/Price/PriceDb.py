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

    def __init__(self, path):
        self.path = path
        self.name = None
        self.size_files_optional = None
        self.type = None
        self.size = None
        self.size_files = None
        self.modify = None
        self.priceID = None
        self.price = 0

    def load(self):
        self.name = self.getName()
        self.type = self.getType()
        self.size = self.getSize()
        self.modify = int(time.time())

    def reload(self):
        # reload size and modify time
        self.size = self.getSize()
        self.modify = int(time.time())

    def getName(self):
        if os.path.isfile(self.path):
            fullname = os.path.split(self.path)[-1]
            if '.' in fullname:
                return fullname.split('.')[0]
            else:
                return fullname
        else:
            return None

    def getType(self):
        if os.path.isfile(self.path):
            return os.path.splitext(self.path)[-1][1:]
        else:
            return None

    # return size of files in kb
    def getSize(self):
        if os.path.isfile(self.path):
            return os.path.getsize(self.path)
        else:
            return None


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
            self.checkTables() # create database
        except Exception, err:
            self.log.error("Error loading price.db: %s, rebuilding..." % Debug.formatException(err))
            self.close()
            os.unlink(self.dbpath)  # Remove and try again
            self.schema = self.getSchema()
            self.checkTables()
        self.prices = {} # a record is a price, type is {"relpath:price}

    def getSchema(self):
        schema = {}
        schema["db_name"] = "PriceDb"
        schema["version"] = 1
        schema["tables"] = {}

        schema["tables"]["price"] = {
            "cols": [
                ["price_id", "INTEGER PRIMARY KEY AUTOINCREMENT"],# set priceID increase self,so don't care this value
                ["path", "TEXT UNIQUE NOT NULL"],
                ["name","TEXT"],
                ["size", "INTEGER"],
                ["price", "REAL"],
                ["size_files", "INTEGER"],
                ["size_files_optional", "INTEGER"],
                ["file_type", "TEXT"],
                ["modified", "INTEGER"]
            ],
            "indexes": [
                "CREATE UNIQUE INDEX price_key ON price (path)",
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

    def setPrice(self, path, price):
        if path in self.prices.keys():
            temp_price = self.prices.get(path)
        else:
            self.log.warning("Error get %s from self.prices" % (path))
            temp_price = Price(path)
            temp_price.load()
        temp_price.price = price
        try:
            self.insertOrUpdate("price", {
                "name": temp_price.name,
                "path": temp_price.path,
                "price": temp_price.price,
                "size": temp_price.size,
                "file_type": temp_price.type,
                "size_files_optional": temp_price.size_files_optional,
                "size_files": temp_price.size_files,
                "modified": int(temp_price.modify)

            }, {
                 "path": temp_price.path
                 })
            self.prices[path] = temp_price
            self.log.info("Success set %s price successful!" % (path))
            return True
        except Exception as e:
            self.log.error("Error set {}'s price.Exception is {}".format(path, e))
            return False

    def deletePrice(self, path):
        if path in self.prices.keys():
            self.prices.pop(path)
            self.log.info("Delete %s from self.prices success" % (path))
        else:
            # self.log
            self.log.warning("There is not %s in self.prices success" % (path))
        res = self.execute("SELECT * FROM price WHERE ?", {"path": path})
        if res.fetchone():
            if self.execute("DELETE FROM price WHERE ?", {"path": path}):
                self.log.info("Success delete %s from self.prices success" % (path))
                return True
            else:
                self.log.error("Error delete %s from self.prices faild!" % (path))
                return False
        else:
            self.log.warning("Excess delete {}:not set ".format(path))
            return True

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
            path = os.path.join(self.site_path, row["path"])
            self.prices[row["path"]] = Price(path)

            self.prices[row["path"]].priceID = row["price_id"]
            self.prices[row["path"]].relpath = row["path"]
            self.prices[row["path"]].name = row["name"]
            self.prices[row["path"]].size = row["size"]
            self.prices[row["path"]].price = row["price"]
            self.prices[row["path"]].size_files = row["size_files"]
            self.prices[row["path"]].size_files_optional = row["size_files_optional"]
            self.prices[row["path"]].type = row["file_type"]
            self.prices[row["path"]].modified = row["modified"]

    def getSetting(self, path):
        if path in self.prices.keys():
            return self.prices.get(path)
        else:
            res = self.execute(
                "SELECT * FROM price WHERE ?",
                {"path": path}
            )
            row = res.fetchone()  # get result
            if row:
                return row
            else:
                return None

price_dbs = {}

# check the sqlite3 is existed, otherwise create database
def getPriceDb(address=config.homepage):

    address_dir = os.path.join(config.data_dir, address)
    path = os.path.join(address_dir, 'price.db')

    if address not in price_dbs:
        price_dbs[address] = PriceDb(path, address)
    return price_dbs[address]

getPriceDb()


