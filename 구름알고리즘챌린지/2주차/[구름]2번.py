# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n=int(input())
s=input()

cnt=0
flag=0
for i in range(len(s)-1):
	if not flag:
		cnt+=1
	
	if s[i]==s[i+1]:
		flag=1
	else:
		flag=0

if not flag:
	cnt+=1
		
print(cnt)