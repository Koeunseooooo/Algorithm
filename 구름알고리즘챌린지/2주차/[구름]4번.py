# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, b_n = map(int, input().split())
arr = [[0 for j in range(n)] for i in range(n)]

for i in range(b_n):
	a, b = map(int, input().split())
	a=a-1
	b=b-1
	arr[a][b]+=1
	if a+1 < b_n and a+1 >= 0:
		arr[a+1][b]+=1
	if a-1 >= 0:
		arr[a-1][b]+=1
	if b+1 < b_n :
		arr[a][b+1]+=1
	if b-1 >= 0:
		arr[a][b-1]+=1
		
result=sum(arr,[])
print(sum(result))