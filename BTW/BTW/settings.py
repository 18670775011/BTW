# -*- coding: utf-8 -*-

# Scrapy settings for BTW project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BTW'

SPIDER_MODULES = ['BTW.spiders']
NEWSPIDER_MODULE = 'BTW.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'BTW (+http://www.yourdomain.com)'
# 所有的都使用该请求头
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 150

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 150
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-CN,zh;q=0.9',
   'Cache-Control': 'no-cache',
   'Connection': 'keep-alive',
   'Pragma': 'no-cache',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BTW.middlewares.BtwSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'BTW.middlewares.BtwDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'BTW.pipelines.BtwPipeline': 200,
   # 'BTW.pipelines.BtwImage': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 图片下载目录
IMAGES_STORE = r'G:\BTW'
# 图片过滤器，最小高度和宽度
IMAGES_MIN_HEIGHT = 850
IMAGES_MIN_WIDTH = 600
# 允许重定向
MEDIA_ALLOW_REDIRECTS = True


# 超时下载设置
RETRY_ENABLED = True  # 重试
RETRY_TIMES = 100


# 关闭日志或调整Debug级别

LOG_LEVEL = 'ERROR'
"""
CRITICAL - 严重错误
ERROR - 一般错误
WARNING - 警告信息
INFO - 一般信息
DEBUG - 调试信息
"""

# 日志文件
LOG_FILE = 'btw.log'

# 是否启用日志（创建日志后，不需开启，进行配置）
LOG_ENABLED = True  # （默认为True，启用日志）

# 如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中
LOG_STDOUT = False

# 日志编码
LOG_ENCODING = 'utf-8'

# MongoDB配置
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "btw"  # 库名
MONGO_COLL = "ImgInfo"  # collection名


