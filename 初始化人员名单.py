#!/usr/bin/env python
# -*- coding: gbk -*-
#
#  ��ʼ����Ա����.py
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

number_0={'����':'���'}
# �������г�Ա���������б仯�������޸�
import json
parcipants=json.dumps(number_0,ensure_ascii='Flase')
file_name=('X:/X/X/paticipants.json')
# ������Ҫ�����λ��
with open(file_name,'w') as f:
	f.write(parcipants)
	f.close()
# ת����JSON�ļ�
print('���ǳɹ���д���˲μ���������')
