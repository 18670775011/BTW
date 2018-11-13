# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


# 图片url处理
def get_url(value):
    try:
        classid = re.match('.+\?classid=(\d+)&.+', value).group(1)
        img_id = re.match('.+\?classid=\d+&amp;id=(\d+)&.+', value).group(1)
    except AttributeError:
        classid = re.match('.+\?classid=(\d+)&.+', value).group(1)
        img_id = re.match('.+\?classid=\d+&id=(\d+)&.+', value).group(1)
    url = 'http://pic.netbian.com/downpic.php?id={}&classid={}'.format(img_id, classid)
    return url


# img_type为空
def null_type(value):
    if not value:
        value = '其它'
    return value


class BtwItem(scrapy.Item):

    name = scrapy.Field()
    img_url = scrapy.Field(input_processor=MapCompose(get_url), output_processor=TakeFirst())
    img_type = scrapy.Field(input_processor=MapCompose(null_type))
    size = scrapy.Field()       # 图片大小
    resolution = scrapy.Field()  # 分辨率
    upload_time = scrapy.Field()  # 上传时间
    download_tag = scrapy.Field()  # 1表示已经下载， 0表示未下载（默认为1，异常为0）

