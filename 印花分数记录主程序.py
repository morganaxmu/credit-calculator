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
prompt = "\nWelcome!\nEnter 'add' to updata info."
prompt += "\nEnter 'check' to check the result.\nEnter 'quit' to leave.\n"
message=''
# 初始化系统
active = True
while active:
	message=input(prompt)
	if message=='add':
		name=input('Who gets the stamps?\n')
		object=input('Which object?\n')
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
					print(name+" get 1 stamp in "+object)
				else:
					print('You can only get 1 stamp in the same object!')
# 接下来保存结果		
		logs=json.dumps(player_info,ensure_ascii='Flase')
		with open(file_name3,'a') as f:
			f.write(logs)
			f.close()
	if message=='check':
		name=input("Who's credit do you want?\n")
		for i in range(19):
			whom=player_info[i]
			if whom['name']==name:
				credit=whom['TS']
		print(name+' gets '+credit+' !')
	if message=='quit':
		warming = "\nEnd this program will lose all the works!"
		warming += "\nEnter 'Yes' to end it. And delete the log.json!\n"
		tips=input(warming)
		if tips=='Yes':
			active = False
	else:
		continue
