# coding=utf-8
# @File  : PriceDb.py
# @Author: PuJi
# @Date  : 2018/1/19 0019
from Config import config
from Db import Db
from Debug import Debug
import os

class PriceDb(Db):
    def __init__(self, path):
        Db.__init__(self, {"db_name": "PriceDb", "tables": {}}, path)
        self.foreign_keys = True
        try:
            self.schema = self.getSchema()
            self.checkTables() # 创建数据库
        except Exception, err:
            self.log.error("Error loading price.db: %s, rebuilding..." % Debug.formatException(err))
            self.close()
            os.unlink(path)  # Remove and try again
            self.schema = self.getSchema()
            self.checkTables()
        self.site_ids = {}
        self.sites = {}

    def getSchema(self):
        schema = {}
        schema["db_name"] = "PriceDb"
        schema["version"] = 1
        schema["tables"] = {}

        if not self.getTableVersion("site"):
            self.log.debug("Migrating from table version-less content.db")
            version = int(self.execute("PRAGMA user_version").fetchone()[0])
            if version > 0:
                self.checkTables()
                self.execute("INSERT INTO keyvalue ?", {"json_id": 0, "key": "table.site.version", "value": 1})
                self.execute("INSERT INTO keyvalue ?", {"json_id": 0, "key": "table.content.version", "value": 1})

        schema["tables"]["site"] = {
            "cols": [
                ["site_id", "INTEGER  PRIMARY KEY ASC NOT NULL UNIQUE"],
                ["address", "TEXT NOT NULL"]
            ],
            "indexes": [
                "CREATE UNIQUE INDEX site_address ON site (address)"
            ],
            "schema_changed": 1
        }

        schema["tables"]["content"] = {
            "cols": [
                ["content_id", "INTEGER PRIMARY KEY UNIQUE NOT NULL"],
                ["site_id", "INTEGER REFERENCES site (site_id) ON DELETE CASCADE"],
                ["inner_path", "TEXT"],
                ["size", "INTEGER"],
                ["size_files", "INTEGER"],
                ["size_files_optional", "INTEGER"],
                ["modified", "INTEGER"]
            ],
            "indexes": [
                "CREATE UNIQUE INDEX content_key ON content (site_id, inner_path)",
                "CREATE INDEX content_modified ON content (site_id, modified)"
            ],
            "schema_changed": 1
        }

        return schema

price_dbs = {}

# 检查数据库文件是否存在，否则创建数据库
def getPriceDb(address, path=None):
    if not path:
        path = os.path.join(config.data_dir, address, 'price.db')
    if path not in price_dbs:
        price_dbs[path] = PriceDb(path)
    return price_dbs[path]