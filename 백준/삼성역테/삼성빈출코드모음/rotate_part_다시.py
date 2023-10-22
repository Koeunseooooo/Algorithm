arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]] #5*4배열

n=5 # 가로
m=4 # 세로
start=2
end=5
dist=end-start

# 90도 방향회전
# old i,j
# new j N-i-1

for i in range(n):
    for j in range(m):
        arr[i]