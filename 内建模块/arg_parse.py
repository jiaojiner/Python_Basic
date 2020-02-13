#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


def qyt_argparse(host, filename, iface):
    print(host)
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    # b1 = "python arg_parse.py ipaddress -f filename -i interface"
    # parser = ArgumentParser(usage=b1)
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="Write content to FILE", default='1.txt', type=str)
    parser.add_argument("-i", "--interface", dest="iface", help="Specify an interface", default=1, type=int)
    parser.add_argument(nargs='?', dest="host", help="Specify an host", default='10.1.1.1', type=str)
    # parser.add_argument(nargs='*', dest="hosts", help="Specify an host", default='10.1.1.1', type=str)
    args = parser.parse_args()

    qyt_argparse(args.host, args.filename, args.iface)
    # qyt_argparse(args.hosts, args.filename, args.iface)
