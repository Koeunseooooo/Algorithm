# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t=int(input())
result={}
for i in range(t):
	n=int(input())
	scores=list(map(int,input().split()))
	avg=sum(scores)/len(scores)
	count=0
	for score in scores:
		if score >= avg:
			count=count+1
	print("{0}/{1}".format(count,len(scores)))