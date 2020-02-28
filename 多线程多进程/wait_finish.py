#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from module import module
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import random
import time

if __name__ == '__main__':
    # 多进程
    # freeze_support()  # Windows 平台要加上这句，并且一定要放在if __name__ == '__main__':下,才能避免 RuntimeError
    # pool = ProcessPool()  # 有效控制并发进程或者线程数，默认为内核数(推荐)
    # cpus = multiprocessing.cpu_count()#得到内核数的方法

    # 多线程
    pool = ThreadPool(processes=5)

    result = pool.apply_async(module, args=(10, 20, 30))

    # pool.apply_async 采用异步方式调用
    # task，pool.apply 则是同步方式调用。
    # 同步方式意味着下一个 task 需要等待上一个 task 完成后才能开始运行，这显然不是我们想要的功能，所以采用异步方式连续地提交任务。

    # pool.close()
    # pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    while True:
        print(result.ready())
        time.sleep(1)
