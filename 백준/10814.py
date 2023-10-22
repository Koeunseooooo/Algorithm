import heapq
n=int(input())

heap=[]
for i in range(n):
    age,name=input().split()
    age=int(age)
    heapq.heappush(heap,(age,i,name))

while heap:
    age, _, name=heapq.heappop(heap)
    print(age,name)