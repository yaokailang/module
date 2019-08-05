# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
<<<<<<< Updated upstream

=======
import pymongo

#下载图片
>>>>>>> Stashed changes
class Spider360Pipeline(ImagesPipeline):
    def file_path(self,request,response=None,info=None):
        url = request.url
        fril_name = url.split('/')[-1]
        return fril_name

    def item_completed(self, results, item, info):
        image_paths = [x['path']for ok ,x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])
<<<<<<< Updated upstream
=======


#保存到数据库
class MongodbPipelins(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['example']
        self.table = self.db['content']

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        return item

>>>>>>> Stashed changes
