#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from xml.dom.minidom import Document

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)  # 创建根

Name = doc.createElement('姓名')
Name.setAttribute('name', '较劲儿')

root.appendChild(Name)  # 在根下创建
#############################################
Skills = doc.createElement('网络相关')
Skills.setAttribute('name', '网络技能')

Name.appendChild(Skills)  # 在姓名下创建网络相关

Skill_Description = doc.createElement('网络相关简介')
Skills.appendChild(Skill_Description)  # 在网络相关下创建网络相关简介

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉TCP/IP协议族，掌握路由交换技术\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)  # 创建技能简介的文本TEXT

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)  # 在网络相关下创建技能分类

skill_Name = doc.createElement('路由交换')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)  # 在技能分类下创建路由交换技能

skill_Name = doc.createElement('TCP/IP')
skill_Name.setAttribute('level', '精通')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('OSI')
skill_Name.setAttribute('level', '精通')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('IPv6')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('网络安全相关')
Skills.setAttribute('name', '网络安全技能')

Name.appendChild(Skills)

Skill_Description = doc.createElement('网络安全相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉渗透测试相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('Hacker')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('Kali')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('OWASP')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('数据库相关')
Skills.setAttribute('name', '数据库相关')

Name.appendChild(Skills)

Skill_Description = doc.createElement('数据库相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉数据库相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('Mysql')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('Sqlserver')
skill_Name.setAttribute('level', '了解')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('sqlite')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('语言相关')
Skills.setAttribute('name', '语言相关')

Name.appendChild(Skills)

Skill_Description = doc.createElement('语言相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉python相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('python')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('shell')
skill_Name.setAttribute('level', '了解')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('系统相关')
Skills.setAttribute('name', '系统相关')

Name.appendChild(Skills)

Skill_Description = doc.createElement('系统相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉各类系统相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('Linux')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('windows')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('虚拟化与云计算相关')
Skills.setAttribute('name', '虚拟化与云计算相关')

Name.appendChild(Skills)

Skill_Description = doc.createElement('虚拟化与云计算相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉虚拟化相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('Vmware')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('FusionComputer')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

#############################################
Skills = doc.createElement('办公相关')
Skills.setAttribute('name', '办公相关')

Name.appendChild(Skills)

Skill_Description = doc.createElement('办公相关简介')
Skills.appendChild(Skill_Description)

Skill_Description_Text = doc.createTextNode('\n\t\t\t\t熟悉office相关技能\n\t\t\t')
Skill_Description.appendChild(Skill_Description_Text)

skill = doc.createElement('技能分类')
skill.setAttribute('name', '技能分类')
Skills.appendChild(skill)

skill_Name = doc.createElement('office')
skill_Name.setAttribute('level', '熟悉')
skill.appendChild(skill_Name)

skill_Name = doc.createElement('Adobe')
skill_Name.setAttribute('level', '了解')
skill.appendChild(skill_Name)

XML_File = open('XML_4_Write.xml', 'w', encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()
