#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

# from scapy.all import *
import logging
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, 1
    else:
        return ip, 0


if __name__ == '__main__':
    import sys
    result = qytang_ping(sys.argv[1])
    # print(result)
    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')
