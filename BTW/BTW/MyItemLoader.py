from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


# 去除空格\a0
def space_convert(value):
    res_value = ''.join(value.split())
    return res_value


class MyItemLoad(ItemLoader):
    default_output_processor = TakeFirst()
