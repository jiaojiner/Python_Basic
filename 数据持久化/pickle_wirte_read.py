#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


import pickle
import time

db = {'192.168.98.129': '可达', '192.168.98.128': '可达', '192.168.98.12': '不可达'}

# 先将字典内容写进文件后再重新读取文件内容
# dbfile = open('pickle_test.pl', 'bw')
# pickle.dump(db, dbfile)
# dbfile.close()
# print('写入程序执行完毕')
# print('='*20)
# time.sleep(2)
# print('即将开始读取文件')
# dbfile_read = open('pickle_test.pl', 'rb')
# read_result = pickle.load(dbfile_read)
# print(read_result)
# dbfile_read.close()

# 直接以追加的方式写入文件，然后移动指针到文件首部进行读取
print('开始写入文件！')
dbfile = open('pickle_test.pl', 'ba+')
pickle.dump(db, dbfile)
time.sleep(2)
print('写入完毕，开始移动指针位置！')
dbfile.seek(0, 0)
print('指针位置移动到：', dbfile.tell())
time.sleep(2)
print('开始读取文件内容！')
read_result = pickle.load(dbfile)
print(read_result)
time.sleep(2)
print('读取文件完成，关闭文件')
dbfile.close()

