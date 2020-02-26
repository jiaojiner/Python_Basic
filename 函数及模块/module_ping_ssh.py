#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from scapy_ping import ping
from paramiko_ssh import ssh


def ssh(ip_list1, username, password, cmd):
    for ip in ip_list1:
        ping_result = ping(ip)
        if ping_result[1] == 1:
            print(ping_result[0], '可达！')
            print('尝试登录', ping_result[0], '执行', cmd, '结果如下：')
            print(ssh(ip_list1[0], username=username, password=password, cmd=cmd))
        else:
            print(ping_result[0], ' 不可达！')


if __name__ == '__main__':
    ip_list1 = ['192.168.98.129', '127.0.0.1']
    username = 'root'
    password = '1'
    ssh(ip_list1, username, password, 'ls')