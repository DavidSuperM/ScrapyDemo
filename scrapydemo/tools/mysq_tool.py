# -*- coding: utf-8 -*-
import logging
import os
import time

import pymysql

from scrapydemo import settings


class MysqlTool(object):

    @classmethod
    def get_connection(cls):
        # 这个需要配环境变量，根据环境变量的不同来获得不同的数据用户名密码
        hostname = os.getenv('HOSTNAME', '127-0-0-1')
        if hostname == '127-0-0-1':
            host = settings.MYSQL_HOST
            port = settings.MYSQL_PORT
            user = settings.MYSQL_USER
            pwd = settings.MYSQL_PASSWORD
            db_name = settings.MYSQL_DB_NAME
        elif hostname == '11-11-11-11':
            host = settings.TEST_MYSQL_HOST
            port = settings.TEST_MYSQL_PORT
            user = settings.TEST_MYSQL_USER
            pwd = settings.TEST_MYSQL_PASSWORD
            db_name = settings.TEST_MYSQL_DB_NAME
        else:
            host = settings.OL_MYSQL_HOST
            port = settings.OL_MYSQL_PORT
            user = settings.OL_MYSQL_USER
            pwd = settings.OL_MYSQL_PASSWORD
            db_name = settings.OL_MYSQL_DB_NAME
        conn = pymysql.connect(host=host, port=port, db=db_name, user=user, passwd=pwd, charset='utf8', autocommit=True)
        return conn

    @classmethod
    def close_connection(cls, conn, cur):
        cur.close()
        conn.close()

    @classmethod
    def get_ip_list(cls, str):
        try:
            ip_list = []
            conn = MysqlTool.get_connection()
            cur = conn.cursor()
            # sql = "select ip from ip_table where type=%s  and status >=0"
            sql = ''
            cur.execute(sql, (str))
            all_data = cur.fetchall()
            for item in all_data:
                ip_list.append(item[0])
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))
        finally:
            MysqlTool.close_connection(conn, cur)
        return ip_list

    @classmethod
    def insert_test(cls, list):
        try:
            conn = MysqlTool.get_connection()
            cur = conn.cursor()
            params = []
            for item in list:
                params.append((item, 'aa', 0))
            # sql = "insert ignore into book_table(book_name, author, status) VALUES (%s, %s, %s)"
            sql = ''
            cur.executemany(sql, params)
            return
        except Exception as e:
            logging.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Exception' + str(e))
        finally:
            MysqlTool.close_connection(conn, cur)
