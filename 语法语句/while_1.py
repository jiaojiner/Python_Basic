#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import time

while True:
    try:  # 尝试去执行
        time.sleep(2)
        print('请输入Ctrl + C来停止这个循环')
    except KeyboardInterrupt:
        # 如果出现KeyboardInterrupt异常的处理方法
        print("接收到管理员的ctrl+c!")
        print("退出程序")
        break
