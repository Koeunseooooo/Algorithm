# 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례 = O(n)

n=int(input())
x,y=1,1
plans=input().split()

# R L U D에 따른 이동 방향
## 이동방향 헷갈리지 말것..
dx=[0,0,-1,1]
dy=[1,-1,0,0]
move_type=['R','L','U','D']

for plan in plans:
    for i in range(len(move_type)):
        if plan==move_type[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    # 공간이 벗어나는 경우는 무시
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x=nx
    y=ny

print(x,y)
    


ㅁ