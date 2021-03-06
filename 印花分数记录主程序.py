#!/usr/bin/env python
# -*- coding: gbk -*-
#
#  印花分数记录主程序.py
#  
#  Copyright 2018 morganaxmu
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import json
file_name=('X:/X/X/paticipants.json')
file_name2=('X:/X/X/result.json')
file_name3=('X:/X/X/log.json')
# 输入自己的文件路径
# Python里头\r好像是提前到最前面，所以路径里面的R要大写, 或直接用/
info=open(file_name,'r',encoding='utf-8')
player=json.load(info)
# 载入参与者列表
namelist=[]
player_info=[]
with open(file_name2,'w') as f:
		f.write(' ')
		f.close()
# 初始化
for key in player:
	new_ass=key
	namelist.append(new_ass)
# range()中的参数请根据参加者人数进行确定
for i in range(19):
	intermedia={'name':namelist[i],'number':i+1,'A':'0','B':'0','C':'0',
	'D':'0','E':'0','TS':'0'}
	player_info.append(intermedia)
	intermedia2=json.dumps(intermedia,ensure_ascii='Flase')
	with open(file_name2,'a') as f:
		f.write(intermedia2)
		f.close()
# 根据参与者列表，创建对应个人信息，接下来进入主循环
prompt = "\n欢迎!\n输入'add'指令以为某人增加印花."
prompt += "\n输入'check'来查看某人的印花数量。\n输入'quit'终止程序\n"
message=''
# 初始化系统
active = True
while active:
	message=input(prompt)
	if message=='add':
		name=input('谁获得了印花？\n')
		object=input('在哪个项目上？\n')
		for i in range(19):
			whom=player_info[i]
			if whom['name']==name:
				whom=player_info[i]
				if whom[object]!='1':
					whom[object]='1'
					TS=int(whom['TS'])
					TS=TS+1
					TS=str(TS)
					whom['TS']=TS
					print(name+"在"+object+"得到了一枚印花")
				else:
					print('你只能在一个项目上得到一枚印花！')
			else:
				print('输入不合法')
				continue
# 接下来保存结果		
		logs=json.dumps(player_info,ensure_ascii='Flase')
		with open(file_name3,'w') as f:
			f.write(logs)
			f.close()
	if message=='check':
		name=input("你想查询谁？\n")
		for i in range(19):
			whom=player_info[i]
			if whom['name']==name:
				credit=whom['TS']
			else:
				print('输入不合法')
				credit='nothing'
				continue
			print(name+' gets '+credit+' !')
	if message=='quit':
		warming = "\n结束本程序会丢失所有未储存的信息！"
		warming += "\n输入'Yes'来确定结束程序，不要忘记清空log.json!\n"
		tips=input(warming)
		if tips=='Yes':
			active = False
		else:
			print('输入不合法')
			continue
	else:
		print('输入不合法')
		continue
