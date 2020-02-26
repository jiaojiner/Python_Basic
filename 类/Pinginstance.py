#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


from Pingclass import Pingclass

if __name__ == '__main__':
    ping = Pingclass('192.168.98.1', '192.168.98.29')
    # ping.ping_one()
    # ping.src('1.1.1.1')
    ping.ping()
