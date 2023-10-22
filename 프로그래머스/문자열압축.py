import heapq
heap=[]


heapq.heappush(heap,(1,2,2))
heapq.heappush(heap, (1, 1, 2))
heapq.heappush(heap, (1, 2, 1))

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))