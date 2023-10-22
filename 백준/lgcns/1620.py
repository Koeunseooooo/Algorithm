from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
dogam1 = dict()
dogam2 = dict()

for i in range(1, n + 1):
    name = input().rstrip()
    dogam1[i] = name
    dogam2[name] = i


for _ in range(m):
    comm = input().rstrip()
    # print("comm", comm)
    if comm.isdigit():
        print(dogam1[int(comm)])
    else:
        print(dogam2[comm])

# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# dict = {}

# for i in range(1, n + 1):
#     a = input().rstrip()
#     dict[i] = a
#     dict[a] = i

# for i in range(m):
#     quest = input().rstrip()
#     if quest.isdigit():
#         print(dict[int(quest)])
#     else:
#         print(dict[quest])
