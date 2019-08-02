# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from json import loads
from ..items import Spider360Item

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    q=0
    def start_requests(self):
        base_url = 'http://image.so.com/zjl?'
        param = {'ch' : 'wallpaper'}
        for page in range(100):
            param['sn'] = page * 30
            param['ph'] = 30
            param['prevsn'] = page * 30 - 30
            full_url = base_url + urlencode(param)
            yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        model_dict = loads(response.text)
        self.q+=1
        print(self.q)
        for elem in model_dict['list']:
            item = Spider360Item()
            item['title'] = elem['title']
            item['url'] = elem['qhimg_url']
            item['id'] = elem['id']
            item['label'] = elem['label']
            yield item

