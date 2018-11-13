# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.conf import settings

Cookies = {'__cfduid' :'d74052ed4d48a524edd9e34115b1152721540301058',
 'yjs_id': '80528b269079d4c0e66cad76c20fe619',
 'PHPSESSID': '101046871400c6285f64eecb3fee14bd',
 'Hm_lvt_24b7d5cc1b26f24f256b6869b069278e':'1540365491',
 'Hm_lpvt_24b7d5cc1b26f24f256b6869b069278e':'1540365546',
 'zkhanecookieclassrecord':'%2C55%2C66%2C60%2C65%2C54%2C63%2C',
 'ctrl_time':'1',
 'Hm_lvt_526caf4e20c21f06a4e9209712d6a20e':'1539394620,1540276266',
 'zkhanmlusername':'qq_Ail329',
 'zkhanmluserid':'605948',
 'zkhanmlgroupid':'3',
 'zkhanmlrnd':'XJFN5K6k3jkXukmhYfkP',
 'zkhanmlauth':'344a2d12fcd6612c2bd39caae7299bcf',
 'security_session_verify':'1283fa00efbfb00c24c219b32b9a41b8',
 'Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e':'1540516070'
    }


# 数据存储
class BtwPipeline(object):
    def __init__(self):
        host = settings["MONGO_HOST"]
        port = settings["MONGO_PORT"]
        dbname = settings["MONGO_DB"]
        collname = settings["MONGO_COLL"]
        # 连接数据库
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.coll = db[collname]
        self.count = 0

    def process_item(self, item, spider):
        data = dict(item)  # 把item转换成字典形式
        try:
            self.coll.insert(data)  # 向数据库插入一条记录
            self.count += 1
        except:
            raise IOError
        if not self.count % 100:
            print("已获取数据：%d条" % self.count)
        return item


class BtwImage(ImagesPipeline):

    # 图片下载
    def get_media_requests(self, item, info):
        yield Request(url=item['img_url'], cookies=Cookies, meta={'name': item['name'], 'img_type': item['img_type']})

    # 是否下载成功
    def item_completed(self, results, item, info):
        """results是一个list 第一个为图片下载状态,对应OK
        第二个是一个tupled其中可以为path的字段对应存储路径,
        而item['front_image_path']是我们自定义字段,保存在item中
        """
        front_image_path = [x['path'] for ok, x in results if ok]
        if front_image_path:
            print(str(front_image_path) + '下载成功！')
        return item

    # 图片重命名
    def file_path(self, request, response=None, info=None):
        name = request.meta['name']
        img_type = request.meta['img_type']  # 用分类来做文件夹名称
        # 清洗Windows系统的文件夹非法字符，避免无法创建目录
        folder_strip = re.sub(r'[？\\*|“<>:/]', '', str(img_type))
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}.jpg'.format(folder_strip, name)
        return filename