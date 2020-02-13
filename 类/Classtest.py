#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


class Person:
    """
    一般Person：数据+逻辑
    """
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s: %s, %s >' % (self.__class__.__name__, self.name, self.job, self.pay)


class Manager(Person):
    """
    带有自定义加薪的Person
    继承了通用的lastname, str
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(sue, sue.pay, sue.lastname())

    for obj in (bob, sue, tom):
        obj.giveraise(.10)
        print(obj)
