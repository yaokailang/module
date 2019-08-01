# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


#保存的Mysql数据库中
# class DoubandushuPipeline(object):
#     def __init__(self):
#         self.conn = pymysql.connect('127.0.0.1', 'root', '19990811',
#                                   'douban', 3306, charset = 'utf8')
#         self.curspr = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         insert_sql = 'insert into duoban(title, url, grade, author, brief)' \
#                      'valuse (%s, %s, %s, %s, %s)'
#         self.curspr.execute(insert_sql, (item['title'], item['url'],item['grade'],
#                                           item['author'], item['brief']))
#
#     def close_spider(self,spider):
#         self.curspr.close()
#         self.conn.close()

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
