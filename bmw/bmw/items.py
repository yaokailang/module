# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BmwItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()     #分类
    urls =scrapy.Field()      #url
    pass
