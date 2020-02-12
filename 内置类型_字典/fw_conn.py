#!/usr/bin/env python
# -*- enconding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import re

str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

list1 = str1.split('\n')
# print(list1)
dict1 = {}

for x in list1:
    result = re.match('(TCP|UDP).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\
.*bytes\s(\d*).*', x).groups()
    print(result)
    dict_key = result[0], result[1], result[2], result[3], result[4]
    dict_values = result[-1]
    dict1[dict_key] = dict_values
print('\t''打印字典如下')
print(dict1)

print('\n\n''\t''格式化输入数据：')
print('=' * 120)
for key, vlaues in dict1.items():
    print(
        '{0:>8s} : {1:<5s} | {2:>8s} : {3:<12s} | {4:>8s} : {5:<5s} | {6:>8s} : {7:<12s} | {8:>8s} : {9:<5s} | {10:>5s} : {11:<12s}'.format \
            ('protocol', key[0], 'src_ip', key[1], 'src_p', key[2], 'dst_ip', key[3], 'dst_p', key[4], 'bytes',
             vlaues[-1]))
    print('=' * 120)
