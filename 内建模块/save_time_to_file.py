#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import datetime

datetime_three_result = datetime.datetime.now() - datetime.timedelta(days=3)
othertime_result = str(datetime_three_result)
otherstyletime = datetime_three_result.strftime("%Y-%m-%d %H:%M")
strtime = str(otherstyletime)
# print(type(otherstyletime))
# print(type(othertime_result))
timefile = open('save_threedaysago_time_' + strtime + '.txt', 'w')
timefile.write(othertime_result)
timefile.close()
print('程序执行完成，文件已创建！')
