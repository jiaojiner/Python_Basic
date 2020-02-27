#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


def outer(fun):
    # fun = name
    def inner():
        print("inner is start")
        fun()  # name() --> I am while
        print("inner is done")
        # return "while is cool"
    return inner


def name():
    print("I am while")


# print(name)
# print(outer(name))
print(outer(name)())
# name 是一个普通的函数
# outer(name) 是一个接收name函数作为参数的outer函数的调用，返回inner
# outer(name)() 就是对返回的以name作为嵌套作用域的inner函数的调用
# print(outer(name)()) 打印inner
