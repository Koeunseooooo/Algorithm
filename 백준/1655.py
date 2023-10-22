import heapq
import sys
input = sys.stdin.readline

n=int(input())
leftHeap=[]
rightHeap=[]
for _ in range(n):
    tar=int(input())
    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap,-tar) # 최대힙으로 구성
    else:
        heapq.heappush(rightHeap,tar)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftvalue=heapq.heappop(leftHeap)
        rightvalue=heapq.heappop(rightHeap)
        heapq.heappush(rightHeap,-leftvalue)
        heapq.heappush(leftHeap,-rightvalue) # 최대힙 넣어줄 때 -(음수부호) 붙일 것 !!
    print(-leftHeap[0])