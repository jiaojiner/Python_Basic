#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

# 装饰器实例1---通过装饰器装饰打印效果
# def outer(fun):
#     def inner():
#         print("inner is start")
#         fun()
#         print("inner is done")
#     return inner
#
#
# @outer  # --> name = outer(name)
# def name():
#     print("I am while")
#
#
# name()


# 装饰器实例2---通过装饰器装饰打印效果
# def outer(fun):
#     def inner():
#         print("hello this is our school")
#         fun()
#         print("this teacher is our teacher")
#     return inner
#
#
# @outer  # while_name = outer(name)
# def while_name():
#     print("I am while")
#
#
# @outer  # for_name = outer(name)
# def for_name():
#     print("I am for")
#
#
# while_name()
# print("I am +++++++++++++++++++++++++")
# for_name()


# 装饰器实例2---通过装饰器装饰打印效果
import time


def zs_loger(fun):
    types, data = fun()
    content = "[%s]:[%s]%s"
    return content % (time.ctime(), types, data)


@zs_loger  # loger1 = zs_loger(loger1)
def loger1():
    return "Error", "your password error"


@zs_loger  # loger2 = zs_loger(loger2)
def loger2():
    return "woring", "your are logout"


print(loger1)
print(loger2)
