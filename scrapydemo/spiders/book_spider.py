# -*- coding: utf-8 -*-
import logging
import time
import scrapy

# 以下三行是在 Python2.x版本中解决乱码问题，Python3.x 版本的可以去掉
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

# 目的：根据阅文站点url得到要爬取的书籍名
class BookSpider(scrapy.Spider):
    name = "book_spider"
    # 书籍列表
    book_name_list = []

    def start_requests(self):
        logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "------- book_spider start ------")
        try:
            site_list = ['https://www.qidian.com/rank/yuepiao?page=1']
            name_rule = '//*[@id="rank-view-list"]/div/ul/li[1]/div[2]/h4/a/text()'
            for site in site_list:
                yield scrapy.Request(url=site, callback=self.parse, meta={'name_rule': name_rule})
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))

    # 处理爬取阅文站点书籍的结果
    def parse(self, response):
        try:
            name_rule = response.meta['name_rule']
            # 爬取这一页的10个名字
            for i in range(1, 10):
                length = len(name_rule)
                rule = name_rule[0:36] + str(i) + name_rule[37:length]
                book_name = response.xpath(rule).get()
                self.book_name_list.append(book_name)
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))

    def close(self, reason):
        try:
            # 可以执行mysql插入
            for item in self.book_name_list:
                logging.log(item)
            pass
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))
        logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '--------- book_spider end --------')

