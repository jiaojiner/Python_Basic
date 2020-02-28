#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from scapy_ping import ping
from paramiko_ssh import ssh


def ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = ping(ip)
        if ping_result[1] == 1:
            print(ping_result[0], '可达！')
            print('尝试登录', ping_result[0], '执行', cmd, '结果如下：')
            print(ssh(ping_result[0], username=username, password=password, cmd=cmd))
        else:
            print(ping_result[0], ' 不可达！')


if __name__ == '__main__':
    ip_list = ['192.168.98.128', '192.168.98.12']
    username = 'root'
    password = 'root'
    # ssh(ip_list, username, password, 'dir')
