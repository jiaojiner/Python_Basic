#!/usr/bin/env python
# -*- enconding = utf-8 -*-
#该代码由本人学习时编写，仅供自娱自乐！
#本人QQ：1945962391 
#欢迎留言讨论，共同学习进步！

import os
import time

while True:
    netstat_result_list = (os.popen('netstat -tulnp').read()).split('\n')
    netstat_list = netstat_result_list[2:-1]
    # print(netstat_list)
    for x in netstat_list:
        netstat = (x.split()[3]).split(':')
        if netstat[1] == '80':
            print('HTTP(80)服务已被开启！')
            break
    else:
        time.sleep(1)
        print('等待1秒重新开始检测！')
        continue
    break


# while True:
#     for x in range(10):
#         print(x)
#         # break
#     else:
#         # continue
#         break



