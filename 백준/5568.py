from itertools import permutations
n=int(input())
k=int(input())
arr=[]
for _ in range(n):
    arr.append(input())

candidate=set()
for p in permutations(arr,k):
    candidate.add(''.join(list(p)))

print(len(candidate))