# -*- coding: utf-8 -*-
import scrapy
# 相当于引入一个类
from test2.items import Test2Item
from scrapy.http import Request
import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class test2Spider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["doutula.com","sinaimg.cn"]
    start_urls = ['http://www.doutula.com']
    base = r'F:/giff/'

    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = Test2Item()
        # 创建数组
        items = []
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div

        for box in response.xpath('//div[@class="col-xs-6 col-sm-3"]'):
            item['detailUrl'] = box.xpath('.//img/@data-original').extract()[0]
            item['title'] = box.xpath('.//p/text()').extract()[0]
            fileName = self.base + item['title']
            if not os.path.exists(fileName):
                os.makedirs(fileName)
            item['path'] = fileName + '/' + 'jpg'
            # print(item['detailUrl'])
            items.append(item)

            print(box.xpath)
            yield item
