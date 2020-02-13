#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1


class Pingclass:
    def __init__(self, srcip, dstip, qua=1):
        self.srcip = srcip
        self.ip = dstip
        self.qua = qua
        self.pkt = IP(src=self.srcip, dst=self.ip)/ICMP()

    # def src(self, srcip):
    #     self.srcip = srcip
    #     self.pkt = IP(src=self.srcip, dst=self.ip)/ICMP()

    def ping(self):
        for x in range(self.qua):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print(self.ip, '可达！')
            else:
                print(self.ip, '不可达！')
