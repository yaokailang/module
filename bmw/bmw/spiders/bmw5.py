# -*- coding: utf-8 -*-
import scrapy
from .. items import BmwItem

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        uiboxs=response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            category=uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()     #分类
            urls=uibox.xpath('.//div[@class="uibox-con carpic-list03"]/ul/li/a/img/@src').getall()     #url
            urls=list(map(lambda url:response.urljoin(url),urls))
            item=BmwItem(category=category,urls=urls)
            yield item

