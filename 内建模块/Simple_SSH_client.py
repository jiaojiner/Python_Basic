#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from paramiko_ssh import qytang_ssh

if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = "python Simple_SSH_Client -i ipaddr -u username -p password -c command"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default='10.1.1.1', type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Username", default='root', type=str)
    parser.add_argument("-p", "--password", dest="password", help="SSH Password", default='Cisc0123', type=str)
    parser.add_argument("-c", "--command", dest="command", help="Shell Command", default='ls', type=str)

    args = parser.parse_args()

    print(qytang_ssh(args.ipaddr, args.username, args.password, cmd=args.command))
