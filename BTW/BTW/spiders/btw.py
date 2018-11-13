# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from BTW.MyItemLoader import MyItemLoad
from BTW.items import BtwItem


class BtwSpider(CrawlSpider):
    name = 'btw'
    start_urls = ['http://pic.netbian.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/tupian/\d+.html'), follow=True, callback='parse_item'),  # 主页缩略图链接
        Rule(LinkExtractor(allow=r'/index_\d+.html'), follow=True),  # 下一页

    )

    def parse_item(self, response):
        l = MyItemLoad(item=BtwItem(), response=response)
        l.add_xpath('img_type', r'//*[@id="main"]/div[2]/div[2]/div[2]/p[1]/span/a/text()')
        l.add_xpath('resolution', r'//*[@id="main"]/div[2]/div[2]/div[2]/p[2]/span/text()')
        l.add_xpath('size', r'//*[@id="main"]/div[2]/div[2]/div[2]/p[3]/span/text()')
        l.add_xpath('upload_time', r'//*[@id="main"]/div[2]/div[2]/div[2]/p[4]/span/text()')
        l.add_xpath('name', r'//h1/text()')
        l.add_xpath('img_url', r'/html/body/script[3]/@src')  # 通过输入处理器进行处理
        l.add_value('download_tag', 1)
        return l.load_item()
