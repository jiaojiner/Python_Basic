#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from xml.etree.ElementTree import parse

tree = parse('XML_1_XML.xml')  # 打开分析的XML文件

root = tree.getroot()  # 找到根位置

Skill_dict = {}
for elem in tree.iter(tag='技能分类'):  # 找到技能分类标签(tag)
    skill_list = []
    for elem_in in elem.iter(tag='技能'):  # 找到技能分类标签(tag)下的技能标签
        skill_list.append(elem_in.attrib['name'])  # 找到技能的名字，添加进入列表
    Skill_dict[elem.attrib['name'][:-4]] = skill_list  # 把XX相关技能的相关技能去掉
    # 把技能名称的列表，添加到以技能为键的字典中，作为技能这个键所映射的值！

print(Skill_dict)
