#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import re  # 导入正则表达式模块

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '
str2 = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

# str1_result = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str1).groups()
# str1_result = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str1)
str1_result = re.match('\s*(\w.*\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s.*',
                       str1).groups()
str2_result = re.match('\s*\d+\s*(\w{1,4}\.\w{1,4}\.\w{1,4})\.*', str2).groups()
# print(str1_result)
# print(str2_result)
print('=' * 40)
print('{0:<7s}: {1:<15s}'.format('接口', str1_result[0]))
print('{0:<7s}: {1:<15s}'.format('接口ip地址', str1_result[1]))
print('{0:<7s}: {1:<15s}'.format('接口mac地址', str2_result[0]))
print('{0:<7s}: {1:<15s}'.format('接口状态', str1_result[4]))
print('=' * 40)
print('%-7s : %-15s' % ('接口', str1_result[0]))
print('%-7s : %-15s' % ('接口ip地址', str1_result[1]))
print('%-7s : %-15s' % ('接口mac地址', str2_result[0]))
print('%-7s : %-15s' % ('接口状态', str1_result[4]))
