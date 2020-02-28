#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from random import randint


def scapy_ping_one(host):
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生Ping ID位
    seq_ping = randint(1, 65535)  # 随机产生Ping序列号位
    # 构造Ping数据包
    packet = IP(dst=host, ttl=1) / ICMP(id=id_ping, seq=seq_ping) / b'Welcome'
    ping = sr1(packet, timeout=2, verbose=False)  # 获取响应信息，超时为2秒，关闭详细信息
    if ping:  # 如果有响应信息
        return host, 1
    else:
        return host, 2


if __name__ == '__main__':
    result1 = scapy_ping_one('192.168.98.129')
    if result1[1] == 1:
        print(result1[0], '通！')
    elif result1[1] == 2:
        print(result1[0], '不通！')
    result2 = scapy_ping_one('192.168.98.12')
    if result2[1] == 1:
        print(result2[0], '通！')
    elif result2[1] == 2:
        print(result2[0], '不通！')
