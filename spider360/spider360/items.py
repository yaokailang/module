# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider360Item(scrapy.Item):
    title = scrapy.Field()   #图片标题
    label = scrapy.Field()    #图片的标签
    url = scrapy.Field()    #图片的url
    id = scrapy.Field()    #id
