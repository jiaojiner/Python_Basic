#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import paramiko
import socket


def ssh(ip, username, password, port=22, cmd='show run'):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        if 'Line has invalid autocommand' in x:
            print('命令不能被执行！请检查用户权限！')
        else:
            return x

    except paramiko.ssh_exception.AuthenticationException as e:
        print('认证错误', e)
    except socket.timeout as e:
        print('连接超时', e)
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print('SSH请求被管理过滤', e)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = "python Simple_SSH_Client -i ipaddr -u username -p password -c command"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default='127.0.0.1', type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Username", default='root', type=str)
    parser.add_argument("-p", "--password", dest="password", help="SSH Password", default='root', type=str)
    parser.add_argument("-c", "--command", dest="command", help="Shell Command", default='ls', type=str)

    args = parser.parse_args()

    print(ssh(args.ipaddr, args.username, args.password, cmd=args.command))
