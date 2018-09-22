#!/usr/bin/env python
# -*- coding: gbk -*-
#
#  初始化人员名单.py
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

number_0={'姓名':'编号'}
# 输入所有成员名单，若有变化请自行修改
import json
parcipants=json.dumps(number_0,ensure_ascii='Flase')
file_name=('X:/X/X/paticipants.json')
# 更改你要保存的位置
with open(file_name,'w') as f:
	f.write(parcipants)
	f.close()
# 转换成JSON文件
print('我们成功地写入了参加者名单！')
