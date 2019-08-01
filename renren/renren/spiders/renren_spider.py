# -*- coding: utf-8 -*-
import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url="http://www.renren.com/PLogin.do"
        data={"email":"18820570387",'password':
            "lang19990811"}
        request=scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self,response):
        request=scrapy.Request(url=
                               'http://www.renren.com/971509721/profile',
                               callback=self.parse_profile)
        yield request

    def parse_profile(self,response):
        with open('dp.html','w',encoding='utf-8') as fp:
            fp.write(response.text)

