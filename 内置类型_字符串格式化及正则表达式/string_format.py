#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

department1 = 'HCIE'
department2 = 'Python'
depart1_m = 'jiaojiner'
depart2_m = 'weixu'
course_fees_depart1 = 12313.122
course_fees_depart2 = 1554.121215

# line1 = 'department:%-10s   depart_m:%-10s   fees:%-20.2f' % ('department1','depart1_m',course_fees_depart1)
# line2 = 'department:%-10s   depart_m:%-10s   fees:%-20.2f' % ('department2','depart2_m',course_fees_depart2)

line1 = 'department:{0:<10}   depart_m:{1:<10}   fees:{2:<10.2f}'.format('department1', 'depart1_m',
                                                                         course_fees_depart1)
line2 = 'department:{0:<10}   depart_m:{1:<10}   fees:{2:<10.2f}'.format('department2', 'depart2_m',
                                                                         course_fees_depart2)

length1 = len(line1)
length2 = len(line2)
print('=' * length1)
print(line1)
print(line2)
print('=' * length2)
