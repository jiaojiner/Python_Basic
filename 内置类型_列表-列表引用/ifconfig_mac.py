#!/usr/bin/env python
# -*- enconding = utf-8 -*-
#该代码由本人学习时编写，仅供自娱自乐！
#本人QQ：1945962391 
#欢迎留言讨论，共同学习进步！

import os #引入os模块，可支持执行系统命令
import re #引入正则表达式模块

ifconfig_result = os.popen("ifconfig "+'ens33').read() #执行Linux命令并将结果赋值
# print(ifconfig_result)
list_ifconfig_result = ifconfig_result.split('\n') #将命令返回结果以\n为分割形成列表
# print(list_ifconfig_result)
for x in list_ifconfig_result:
    # print(x.split())
    for mac in x.split():
        # if re.match('.*(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}).*',mac):
        if re.findall('.*(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}).*',mac):
            print('{0:>10s} : {1:<15s}'.format('mac地址为',mac))
            # print('%10s : %-15s' % ('mac地址为',mac))


