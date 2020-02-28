#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


import pickle
import time

db = {'192.168.98.129': '可达', '192.168.98.128': '可达', '192.168.98.12': '不可达'}

# print('测试更改文件内容')
# print('='*20)
# db_file_result = open('pickle_test.pl', 'br')
# db_read_result = pickle.load(db_file_result)
# db_file_result.close()
# db_read_result['192.168.98.12'] = '不可达'
# dbfile_write = open('pickle_test.pl', 'bw')
# pickle.dump(db_read_result, dbfile_write)
# dbfile_write.close()
# print('更改文件程序执行完毕')
# print('='*20)
# time.sleep(2)
# print('即将开始读取文件')
# dbfile_read = open('pickle_test.pl', 'rb')
# read_result = pickle.load(dbfile_read)
# print(read_result)
# dbfile_read.close()

print('读取文件内容：')
dbfile = open('pickle_test.pl', 'ba+')
dbfile.seek(0, 0)
read_result = pickle.load(dbfile)
print(read_result)
time.sleep(2)
print('更改文件内容!')
read_result['192.168.98.12'] = '可达'
# print(dbfile.tell())
dbfile.seek(0, 0)
pickle.dump(read_result, dbfile)
time.sleep(2)
dbfile.seek(0, 0)
print('开始读取文件：')
read_next_result = pickle.load(dbfile)
print(read_result)
dbfile.close()
