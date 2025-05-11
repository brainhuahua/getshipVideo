# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import re

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class GetshipvideoPipeline(FilesPipeline):

    # 依次对视频地址发送请求，meta用于传递视频的文件名
    def get_media_requests(self, item, info):
        # 依次对视频地址发送请求，meta用于传递视频的文件名
        yield scrapy.Request(url="https:"+item['video'], meta={'desc': item['desc']})

    # 返回下载的视频文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        pattern = re.compile(r'[^\u4e00-\u9fa5]')  # 匹配非汉字字符的正则表达式
        text = str(request.meta['desc'])
        text = re.sub(pattern, '', text)
        filename = text+".mp4"  # 获取视频文件名
        return filename  # 返回下载的视频文件名

    def item_completed(self, results, item, info):
        return item
