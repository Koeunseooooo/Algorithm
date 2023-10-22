import heapq
n=int(input())

heap=[]
for _ in range(n):
    num=int(input())
    heapq.heappush(heap,num)

result=0
while True:
    if len(heap)==1:
        break
    card1=heapq.heappop(heap)
    card2=heapq.heappop(heap)
    result+=(card1+card2)
    heapq.heappush(heap,card1+card2)
    # print(result,1)
print(result)