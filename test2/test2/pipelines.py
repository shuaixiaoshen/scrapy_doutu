# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

class Test2Pipeline(object):
    def process_item(self, item, spider):
        path = item['path']
        detailUrl = item['detailUrl']

        # 获取图片
        image = requests.get(detailUrl)
        f = open(path,'wb')
        f.write(image.content)
        f.close()
        return item
