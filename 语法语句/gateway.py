#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import os

route_result = os.popen('route -n').read()
# print(route_result)
route_result_list = route_result.split('\n')
# print(route_result_list)
for x in route_result_list[2:-1]:
    if 'UG' == x.split()[3]:
        print('网关地址为：' + x.split()[1])
