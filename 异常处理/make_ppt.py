#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import os

os.chdir(r'G:\str')

filelist = os.listdir()

maxno = len(filelist)
# print(maxno)
if os.path.exists('PPT.md'):
    os.remove('PPT.md')

pptfile = open('PPT.md', 'w')

for i in range(maxno):
    pptfile.write('![](G:\str\\' + str(i+1) + '.PNG)\r\n\r\n')
pptfile.close()
# print(open('PPT.md', 'rb').read())
# pptfile.close()

