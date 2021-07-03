from collections import deque

#deque는 뱀의 길이 및 위치를 나타낼 때 쓰임

# 진행방향으로부터 왼쪽으로 꺾기
    # 상(0)->우(1)->하(2)->좌(3)
    # 동쪽으로 회전할 경우 : 0 -> 1 -> 2 -> 3
    # 서쪽으로 회전할 경우 : 0 -> 3 -> 2 -> 1

def dir_mapping(cur_dir,c):
    if c=='L': # 서쪽방향
        cur_dir = (cur_dir-1)%4 
        print("?")
    else :  #동쪽방향
        # 진행방향으로부터 오른쪽으로 꺾기
        cur_dir = (cur_dir+1)%4
        print("?")
    return cur_dir



#0:empty, 1:apple, 2:bam~snake~~몸통(그래프의 visited 느낌)
def solution():
    direction = 1 #처음은 동쪽방향으로 설정함
    board[0][0]=2 # (0,0)위치에 뱀이 있다!
    time=0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    y,x=0,0 # 2차원배열속의 좌표 위치를 나타내주는 친구들
    snake_visited=deque([[y,x]])
    
    
    while(True):
        time+=1
        x=x+dx[direction]
        print(x)
        y=y+dy[direction]
        
        if 0<=x<board_size and 0<=y<board_size and board[y][x]!=2:
            if not board[y][x]==1: #사과가 없는경우,,
                tail_y,tail_x=snake_visited.popleft() # 복잡도가 o(n)이라네~
                board[tail_y][tail_x]=0
            board[y][x]=2
            snake_visited.append([y,x])
            
            #방향 재설정
            if time in times.keys():
                print("냐하")
                direction = dir_mapping(direction,times[time])

        else:
            break
    return time


if __name__=="__main__" :
    board_size=int(input())
    board = [[0]*board_size for _ in range(board_size)]

    apple_num=int(input())

    for _ in range(apple_num):
        x,y=map(int,input().split())
        board[x-1][y-1]=1

    dic_num=int(input())

    times={} #key초가 끝난뒤에 value 방향으로 90도 회전
    for _ in range(dic_num):
        x,y=input().split()
        times[int(x)]=y

    print(solution())
    

