# -*- coding: utf-8 -*-

import datetime

# Scrapy settings for scrapydemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapydemo'

SPIDER_MODULES = ['scrapydemo.spiders']
NEWSPIDER_MODULE = 'scrapydemo.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# ## --------------------------

# 本地环境
MYSQL_DB_NAME = 'local_db'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 101
MYSQL_USER = 'u'
MYSQL_PASSWORD = 'u'

# 测试环境
TEST_MYSQL_DB_NAME = 'local_db'
TEST_MYSQL_HOST = '127.0.0.1'
TEST_MYSQL_PORT = 101
TEST_MYSQL_USER = 'u'
TEST_MYSQL_PASSWORD = 'u'

# 线上环境
OL_MYSQL_DB_NAME = 'local_db'
OL_MYSQL_HOST = '127.0.0.1'
OL_MYSQL_PORT = 101
OL_MYSQL_USER = 'u'
OL_MYSQL_PASSWORD = 'u'

# 爬具体网站时使用这些搜索引擎的ua
SEARCH_ENGINE_USER_ANENT_LIST = [
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    # 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Sosospider+(+http://help.soso.com/webspider.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)'
]

HTTPERROR_ALLOWED_CODES = [301, 302]
RETRY_ENABLED = False


LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = './log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
LOG_FILE = log_file_path
# 下载url数据超时时间，默认180s
DOWNLOAD_TIMEOUT = 9

# 设置随机UA
# pip install scrapy-fake-useragent
# pip install Faker
# 加上 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
# 这两行
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapydemo.middlewares.ScrapydemoDownloaderMiddleware': 543,
    'scrapydemo.middlewares.ProxyMiddleware': 543,
}

ITEM_PIPELINES = {
    'scrapydemo.pipelines.ScrapydemoPipeline': 300,
}



# ---------------------

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapydemo (+http://www.yourdomain.com)'



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapydemo.middlewares.ScrapydemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapydemo.middlewares.ScrapydemoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapydemo.pipelines.ScrapydemoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
