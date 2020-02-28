#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import sqlite3
import os

if os.path.exists('sqlite.sqlite'):
    os.remove('sqlite.sqlite')

# Python字典对象，将把它写入SQLite数据库
ip_dict = [{'ip': '192.168.98.129', 'arrive': '可达'}, {'ip': '192.168.98.128', 'arrive': '可达'}]

# 连接SQLite数据库
conn = sqlite3.connect('sqlite.sqlite')
cursor = conn.cursor()

# 执行创建表的任务
cursor.execute("create table test (IP varchar(40), 可达性 varchar(5))")

# 读取Python字典数据，并逐条写入SQLite数据库
for ip in ip_dict:
    # print(ip)
    ip1 = ip['ip']
    arrive = ip['arrive']
    cursor.execute("insert into test values ('%s','%s')" % (ip1, arrive))

# 读取整个sqlite_test表的信息，并且打印
cursor.execute("select * from test")
yourresults = cursor.fetchall()

for ip in yourresults:
    print(ip)

# 基于单一条件搜索数据库表
cursor.execute("select 可达性 from test where ip = '192.168.98.129'")
yourresults = cursor.fetchall()

for arrive1 in yourresults:
    print(arrive1[0])

# 基于多重条件搜索数据库表
cursor.execute("select ip from test where 可达性 = '可达' and ip = '192.168.98.129'")
yourresults = cursor.fetchall()

for ip_result in yourresults:
    print(ip_result[0])

# 删除表
cursor.execute("drop table test")

# 严重注意一定要提交，否则数据不会实际写入数据库
conn.commit()
