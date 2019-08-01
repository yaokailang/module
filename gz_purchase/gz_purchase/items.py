# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GzPurchaseItem(scrapy.Item):
    title = scrapy.Field()          #标题
    content = scrapy.Field()         #内容
    turnover = scrapy.Field()       #发布时间
    urll= scrapy.Field()        #url
