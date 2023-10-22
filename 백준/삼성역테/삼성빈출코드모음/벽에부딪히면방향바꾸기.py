'''
배열은 R*C (행, 열)이라고 가정, dir은 0,1,2,3으로 부여되면서 상, 하, 우, 좌라고 가정
speed는 한번 이동할 때 가야하는 칸수 (낚시왕에서는 상어의 속도)
sd는 이동하려는 방향 (낚시왕에서는 상어의 방향)
'''
R=6
C=5
sd=2
speed=13
x,y=0,0

print(x,y)
print(sd)

ROW = [i for i in range(R)] + [i for i in range(R-2,0,-1)]
COL = [i for i in range(C)] + [i for i in range(C-2,0,-1)]
print(COL)
dirlst = [(-1,0), (1,0), (0,1), (0,-1)] # 0:상, 1:하, 2:우, 3:좌
changedir = {0:1, 1:0, 2:3, 3:2}

di, dj = dirlst[sd] ### 상어의 방향
x, y = (x+di*speed)%len(ROW), (y+dj*speed)%len(COL)
newi, newj = ROW[x], COL[y]
if sd == 0 or sd == 1: ### 상하라면
    if x==0 or x >= R: newsd = changedir[sd] ### 변경
    else: newsd = sd
else: ### 좌우라면
    if y == 0 or y >= C: newsd = changedir[sd]  ### 변경
    else: newsd = sd

print(newi,newj)
print(newsd)
