#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/6 13:16
# @Author : zhaocunwei
# @Version：V 0.1
# @File : mysql_db.py
# @desc :

import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)
