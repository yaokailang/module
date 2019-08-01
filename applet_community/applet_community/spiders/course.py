# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AppletCommunityItem

class CourseSpider(CrawlSpider):
    name = 'course'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+portal\.php\?mod=list\&catid=2\&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-1.html'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()     #标题
        author = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/p/a/text()').get()     #作者
        time = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/p/span/text()').get()    #分布时间
        artice_content = response.xpath("//td[@id='article_content']//text()").getall()     #内容
        content = "".join(artice_content).strip()
        item = AppletCommunityItem(title=title, time=time, author=author,
                         content=content)
        yield item