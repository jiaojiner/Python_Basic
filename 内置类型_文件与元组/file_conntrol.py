#!/usr/bin/env python
# -*- enconding = utf-8 -*-
#该代码由本人学习时编写，仅供自娱自乐！
#本人QQ：1945962391 
#欢迎留言讨论，共同学习进步！

import os

# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
os.chdir('test')                        #切换到test目录下
for file in os.listdir():               #列出目录下的文件名
    if os.path.isfile(file):            #判断文件是否为文件类型
        for line in open(file):         #使用文件迭代器读取文件的每一行
            if 'qytang' in line:        #判断文件中是否存在qytang
                print(file)


# qytang_file_list = []
#
# file_list = os.listdir()
#
# for file in file_list:
#     if os.path.isfile(file):
#         for file_line in open(file):
#             if 'qytang' in file_line:
#                 qytang_file_list.append(file)
#
# print('文件中包含"qytang"关键字的文件为:')
# for file in qytang_file_list:
#     print('\t', end='')
#     print(file)
# print('\n')
