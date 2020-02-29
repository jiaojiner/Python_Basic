#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from xml.dom.minidom import Document
skill_list = {'路由交换': ['RS', 'TCP/IP', 'OSI'], '安全': ['hacker', 'owasp']}

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

Name = doc.createElement('姓名')
Name.setAttribute('name', '较劲儿')

root.appendChild(Name)
#############################################
for skill in skill_list:  # 利用循环将字典中的键值提取，当做姓名下的大标签
    Skill_1 = doc.createElement('技能')
    Skill_1.setAttribute('name', skill)
    Name.appendChild(Skill_1)

    Skill_1_Description = doc.createElement('技能简介')
    Skill_1.appendChild(Skill_1_Description)

    Skill_1_Description_Text = doc.createTextNode('\n\t\t\t\t主要掌握%s相关技能\n\t\t\t' % skill)
    Skill_1_Description.appendChild(Skill_1_Description_Text)

    skill_2 = doc.createElement('技能分类')
    skill_2.setAttribute('name', '%s相关技能' % skill)
    Skill_1.appendChild(skill_2)

    for skill_3 in skill_list[skill]:  # 在大标签下循环出每一个键值对应的value值作为小标签
        skill_Name = doc.createElement('技能')
        skill_Name.setAttribute('name', skill_3)
        skill_2.appendChild(skill_Name)


XML_File = open('XML_6_Auto_Write.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()
