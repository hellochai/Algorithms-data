#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:22
# @Author  : fchai
# @Desc    :
# @File    : about_mysql.py

import pymysql


class Mysql(object):

    def connect(self):
        # self.conn = pymysql.Connection(host='192.168.2.162', user='root',
        #                                password='1111', db='test')

        self.conn = pymysql.Connection(host='192.168.2.162', user='dhlk',
                                       password='dhlktech', db='dhlk_light_cloud')
        return self.conn


mysql = Mysql()
