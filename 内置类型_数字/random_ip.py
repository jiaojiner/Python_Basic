#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import random  # 导入random模块

# ip1 = random.randint(1, 255)  # 在1到255中随机生产一个整数
# ip2 = random.randint(1, 255)
# ip3 = random.randint(1, 255)
# ip4 = random.randint(1, 255)
#
# random_ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)  # 将生成的4个整数转换为字符串并拼接后传递给random_ip
#
# # random_ip = str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.'
# # + str(random.randint(1,255))
#
# print(random_ip)  # 打印所得结果

ip_list = []
for x in range(4):
    ip_list.append(random.randint(1, 255))
print(str(ip_list[0]) + '.' + str(ip_list[1]) + '.' + str(ip_list[2]) + '.' + str(ip_list[3]))
