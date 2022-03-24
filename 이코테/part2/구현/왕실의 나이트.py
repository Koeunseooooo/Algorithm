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




## 답안
'''
input_data=input()
row=int(input_data[1])
col =int(ord(input_data[0])-int(ord('a')+1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt=0
for step in steps:
    next_row=row+step[0]
    next_col=col+step[1]
    
    if next_row >=1 and next_row <=8 and next_row >=1 and next_col <=8:
        cnt+=1
        
print(cnt)'''


# 답안 풀이와 달랐던 점
'''
1) 나는 '상하좌우'처럼 dx,dy에 대하여 각각 리스트 선언 후 이동방향을 기록하도록 하였으나, 
답안 소스코드에서는 steps 리스트안에 튜플형태로 dx,dy가 한번에 포함되어 있었음

2) 나는 예외처리를 or 연산 기준으로 하였으나 답안에서는 and 연산 기준으로 풀었음

=> 스타일의 차이. 딱히 다른건 없어서 그냥 주석으로만 남겨둔다 :) '''