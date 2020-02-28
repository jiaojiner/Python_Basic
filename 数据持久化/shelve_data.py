#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import shelve

db = {'192.168.98.129': '可达', '192.168.98.128': '可达', '192.168.98.12': '不可达'}

db_shelve = shelve.open('db_shelve')
db_shelve['first'] = db
db_shelve.close()
