k = int(input())
n = list(map(int,input().split()))

min = n[0]
for i in range(1,len(n)):
    if min > n[i]:
        min =n[i]
print(min,end=' ')

max = n[0]
for i in range(1,len(n)):
    if max < n[i]:
        max =n[i]
print(max)

# memory 155760ms
# time 664ms
# 정렬 방법 여러 개 찾아보기(다른 사람 풀이 참고)