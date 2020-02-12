#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

list1 = [5, 4, 8, 6, 9, 1, 3, 2]

list2 = list1.copy()  # 拷贝list1并创建一个新的list2列表

list2.sort()  # 对list2列表进行排序，sort方法为升序
# list2.reverse() #对list2列表进行排序，reverse方法为降序

for x in range(len(list1)):
    print(list1[x], list2[x])
