N = int(input())
cnt = 0

for n in range(N):
    flag = True
    S = str(input())
    for i in range(1, len(S)):
        if S[i] in S[0:i] and S[i-1] != S[i]:
            flag = False
    if flag == False:
        cnt += 1

print(N-cnt)
