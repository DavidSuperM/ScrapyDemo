# -*- coding: utf-8 -*-
import logging
import time
import random
import requests
import scrapy
import sys



# 专门处理新加的书，爬取这些书对应的盗版站
class SearchEngineSpider(scrapy.Spider):
    name = "search_engine_spider"
    new_book_list = []
    book_site_list = []

    # 从数据库拿到要爬取的书名和搜索引擎
    def start_requests(self):
        try:
            logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '--------- search_engine_spider start --------')
            self.new_book_list = ['斗破苍穹']
            # rn表示一页几条数据，pn表示第几页
            search_engine_list = ['http://www.baidu.com/s?rn=10&wd=']
            page_number = 1
            for book_item in self.new_book_list:
                for search_engine_url in search_engine_list:
                    for i in range(page_number):
                        search_url = search_engine_url + book_item + '&pn=' + str(i*10)
                        yield scrapy.Request(url=search_url, callback=self.handle_search_engine)
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))

    # 处理搜索引擎的结果，并请求站点数据
    def handle_search_engine(self, response):
        try:
            search_engine_name = 'www.baidu.com'
            rule = '//*[@id="1"]/h3/a/@href'
            for i in range(1, 10):
                url_rule = rule[0:9] + str(1) + rule[10:23]
                site_search_engine_url = response.xpath(url_rule).get()
                if site_search_engine_url is None or (site_search_engine_url[0:3]!='www' and site_search_engine_url[0:4]!='http'):
                    logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'site_search_engine_url err = ' + site_search_engine_url)
                    continue
                site_url = ''
                # 百度的链接会重定向，先拿到重定向后的url
                if search_engine_name == 'www.baidu.com':
                    redirect_response = requests.get(site_search_engine_url, allow_redirects=False)
                    site_url = redirect_response.headers['Location']
                search_engine_ua = random.choice(self.settings.get('SEARCH_ENGINE_USER_ANENT_LIST'))
                search_engine_header = {'User-Agent': search_engine_ua}
                yield scrapy.Request(url=site_url, callback=self.handle_site, headers=search_engine_header)
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))

    # 处理站点的页面数据
    def handle_site(self, response):
        try:
            pass
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))

    def close(self, reason):
        try:
            logging.info('search_engine_spider close')
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))
        logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '--------- search_engine_spider end --------')



