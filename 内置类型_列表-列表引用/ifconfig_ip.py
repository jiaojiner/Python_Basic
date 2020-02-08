#!/usr/bin/env python
# -*- enconding -*-
#该代码由本人学习时编写，仅供自娱自乐！
#本人QQ：1945962391 
#欢迎留言讨论，共同学习进步！

import os #引入os模块，可支持执行系统命令
import re #引入正则表达式模块

ifconfig_result = os.popen("ifconfig "+'ens33').read() #z执行Linux命令并将结果赋值
# print(ifconfig_result)



