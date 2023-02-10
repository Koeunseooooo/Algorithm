from collections import defaultdict
n, m = map(int, input().split())

users = defaultdict(int)
for i in range(n+m):
    user = input()
    users[user] += 1

ans = []
for k, v in users.items():
    if v == 2:
        ans.append(k)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
