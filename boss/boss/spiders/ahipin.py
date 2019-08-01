# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BossItem
import json

class AhipinSpider(CrawlSpider):
    name = 'ahipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1&ka=page-1']

    rules = (
        Rule(LinkExtractor(allow=r'.+/c100010000/\?query=python\&page=.+'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/.+'),callback="parse_job",follow=False)
    )

    def parse_job(self, response):
        title=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[2]/h1/text()').get()     #标题
        alary=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[2]/span/text()').get()     #工资
        job_info=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()').getall()     #工作信息
        job_description=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()').get()     #描述
        team_introduction=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/text()').get()    #介绍
        company_introduction=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[2]/div/text()').get()     #公司介绍

        felare=response.xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[2]/span/text()').getall()
        companyname=response.xpath('//*[@id="main"]/div[3]/div/div[1]/div[2]/div/a[2]/@title').get()           #公司名字
        company_url=response.xpath('//*[@id="main"]/div[3]/div/div[1]/div[2]/p[5]/text()').get()              #公司url


        item=BossItem(title=title,alary=alary,job_info=job_info,job_description=job_description,
                      team_introduction=team_introduction,company_introduction=company_introduction,
                      felare=felare,companyname=companyname,
                      company_url=company_url)
        yield item