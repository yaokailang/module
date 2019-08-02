# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy

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
