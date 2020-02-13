#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


def sys_argv(a, b):
    print(int(a) + int(b))


if __name__ == '__main__':
    import sys

    print(sys.argv[0])
    sys_argv(sys.argv[1], sys.argv[2])