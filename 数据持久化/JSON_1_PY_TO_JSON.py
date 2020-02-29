#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import json

json_dict = {"较劲儿": {"掌握技能": {"路由交换": ["RS", "TCP/IP", "OSI"], "安全": ["hacker", "owasp"]}}}

print('把Python对象转换为JSON格式，并且写入文件')
with open('JSON_file.json', 'w', encoding='utf-8') as f:
    result = json.dump(json_dict, f, ensure_ascii=False)  # 把Python对象转换为JSON格式，并且写入文件

print('='*80)
print('读取JSON文件，并且将json转换为Python对象')
print('-'*80)
with open('JSON_file.json', 'r', encoding='utf-8') as f:
    python_JSON_New = json.load(f)
print('其实\n'+str(python_JSON_New)+'\n是字典', type(python_JSON_New))

print('='*80)
print('可以使用json.dumps方法转换任何Python对象到json字符串')
print('原始python数据：', json_dict)
print('-'*80)
python_JSON = json.dumps(json_dict, ensure_ascii=False)
print('转化后的json数据：', python_JSON)

# srt_result = json.loads(python_JSON)
# print(srt_result)
# print('其实\n'+python_JSON+'\n是字符串', type(python_JSON))


print('='*80)
print('直接把json字符串转换为Python对象')
print('-'*80)

# 严重注意JSON内部必须为双引号
# python中用True，但是JSON中用true
json_str = '{"较劲儿": {"掌握技能": {"路由交换": ["RS", "TCP/IP", "OSI"], "安全": ["hacker", "owasp"]}}}'
print('原始JSON数据：', json_str)
print('-'*80)
STR = json.loads(json_str)
print('转换后的python数据：')
print(STR)
print(type(STR))
