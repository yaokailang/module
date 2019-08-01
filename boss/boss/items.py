# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    title = scrapy.Field()     #标题
    alary = scrapy.Field()     #工资
    job_info = scrapy.Field()        #信息
    job_description = scrapy.Field()         #描述
    team_introduction = scrapy.Field()          #介绍
    company_introduction = scrapy.Field()          #公司介绍
    felare = scrapy.Field()
    companyname = scrapy.Field()      #公司名字
    company_url = scrapy.Field()             #公司url
