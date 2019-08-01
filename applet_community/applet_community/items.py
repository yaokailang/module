# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppletCommunityItem(scrapy.Item):
    title = scrapy.Field()    #标题
    author = scrapy.Field()    #作者
    time = scrapy.Field()      #发表时间
    content = scrapy.Field()     #内容
