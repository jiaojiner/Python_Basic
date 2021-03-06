#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import logging
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, 1
    else:
        return ip, 0


if __name__ == '__main__':
    import sys
    # result = ping(sys.argv[1])  # 将用户输入的数字作为参数传入函数
    result = '192.168.98.129'
    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')
