# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,target=input().split(" ")
cnt=0
for i in range(int(n)):
	user_input=input()
	if target in user_input:
		cnt+=1
		
print(cnt)