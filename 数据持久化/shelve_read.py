#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import shelve

db_read = shelve.open('db_shelve')
for key in db_read:
    print(key, '===>', db_read[key])
db_read.close()
