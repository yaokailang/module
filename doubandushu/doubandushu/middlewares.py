# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json,requests
import datetime
import random

#随机请求头
class DoubandushuDownloadMileware(object):
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; ko; rv:1.9.1b2) Gecko/20081201 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/58.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.59.12) Gecko/20160044 Firefox/52.59.12',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',

    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent


#设置代理
class AhipinSpiderMiddleware(object):
    def __init__(self):
        url = 'http://dev.kdlapi.com/api/getproxy/?orderid=956475957589681&num=1&protocol=1&method=2&an_an=1&an_ha=1&quality=1&format=json&sep=1'
        self.url = url
        self.proxy = ''
        self.expire_datetime = datetime.datetime.now() - datetime.timedelta(seconds=30)
        #self._get_proxy()

    def _get_proxyip(self):
        resp = requests.get(self.url)
        info = json.loads(resp.text)
        proxy_list = info['data']['proxy_list']
        proxyy = str(proxy_list)
        proxy = 'http://'+proxyy[2:-2]
        self.proxy = proxy
        self.expire_datetime = datetime.datetime.now() + datetime.timedelta(seconds=20)

    def _check_expire(self):
        if datetime.datetime.now() >= self.expire_datetime:
            self._get_proxyip()
            print('************************\n','切换代理:',self.proxy)

    def process_request(self,spider,request):
        self._check_expire()
        request.meta['proxy'] = self.proxy