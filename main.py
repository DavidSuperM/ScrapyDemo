import os
import sys
import time
from datetime import datetime
from dateutil.parser import parse

from scrapy.cmdline import execute


if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'book_spider'])
    execute(['scrapy', 'crawl', 'search_engine_spider'])
