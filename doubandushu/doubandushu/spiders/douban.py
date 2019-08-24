# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubandushuItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    rules = (
        Rule(LinkExtractor(allow = r'.*douban\.com/tag/.+'),
             follow = True),
        Rule(LinkExtractor(allow = r'.*douban\.com/subject/\d+/'),
             callback = 'parse_detail', follow=False),
    )

    def parse_detail(self, response):
        if response.status==200:
            try:
                title = response.xpath('//*[@id="wrapper"]/h1/span/text()').get()
                grade = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').get()
                grade_float = float(grade)
                url = response.url
                author = response.xpath('//*[@id="info"]/a[1]/text()').get()
                brief = response.xpath('//div[@class="intro"]').get()
                item = DoubandushuItem(
                    title=title, grade_float=grade_float, url=url,
                    author=author,brief=brief)
                if grade_float >= 8:
                    print(item)
                    yield item
            except:
                print("---------------------------error---------------------------")
        else:
            print('***********************************************************')
