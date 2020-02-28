#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from initdata import db
import pickle
import time

print('测试更改文件内容')
print('='*20)
db_file_result = open('pickle_test.pl', 'br')
db_read_result = pickle.load(db_file_result)
db_file_result.close()
db_read_result['cq_bomb']['pay'] *= 1.6
dbfile_write = open('pickle_test.pl', 'bw')
pickle.dump(db_read_result, dbfile_write)
dbfile_write.close()
print('更改文件程序执行完毕')
print('='*20)
time.sleep(2)
print('即将开始读取文件')
dbfile_read = open('pickle_test.pl', 'rb')
read_result = pickle.load(dbfile_read)
print(read_result)
dbfile_read.close()
