#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import shelve
import time

db_read = shelve.open('db_shelve')
db_update = db_read['first']
db_update['192.168.98.129'] = '不可达'
db_read['first'] = db_update
print('更改文件完毕！')
print('='*20)
time.sleep(2)
print('重新读取文件！')
db_update_new = db_read['first']
print(db_update_new)
db_read.close()
