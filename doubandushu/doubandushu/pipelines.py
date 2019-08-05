# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

#保存到数据库
class MongodbPipelins(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['example']
        self.table = self.db['dbds']

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        return item

#保存为json文件
class JsonPipeline(object):
    def __init__(self):
        self.fp=open("dushu.json",'w',encoding='utf-8')

    def open_spider(self,spider):
        print("这是爬虫开始了......")

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了......")
