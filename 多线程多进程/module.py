#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import time
import os
import threading


def module(x, y, z):
    # 打印进程和线程ID
    # print('pid tid ==>',os.getpid(),threading.currentThread().ident)
    i = 1
    while i < 10:
        sum = x * y * z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)
    # 返回计算结果，进程号，线程号
    return sum, os.getpid(), threading.currentThread().ident


if __name__ == '__main__':
    print(module(1, 2, 3))
