input_data=input()

col=input_data[0] #y (알파벳)
row=input_data[1] #x (숫자)

# 경우의 수는 8가지
dx=[-1,1,-2,-2,1,-1,2,2]
dy=[2,2,1,-1,-2,-2,1,-1]

# print(ord(col)-ord('a'))
x=int(row)
y=ord(col)-ord('a')+1

cnt=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    cnt+=1

print(cnt)