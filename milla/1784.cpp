#include <iostream>
#include <queue>
#define MAX 101

using namespace std;

int N; // 세로
int M; // 가로
int K; // 음식물 쓰레기의 개수
int arr[MAX][MAX] = {0,};
int visited[MAX][MAX] ={0,};
int ny[4]={-1,1,0,0};
int nx[4]={0,0,-1,1};
int answer=0;

bool isValid(int y, int x){
    return ( y>=1 && y<=N && x>=1 && x<=M);
}
int bfs(int y, int x){
    int ans =1;
    visited[y][x]=1;
    queue<pair<int,int>> q;
    q.push({y,x});
    while(!q.empty()){
        int sy = q.front().first;
        int sx = q.front().second;
        q.pop();
        for (int i=0;i<4;i++){
            int ty = ny[i] + sy;
            int tx = nx[i] + sx;
            if(isValid(ty,tx)&& !visited[ty][tx] && arr[ty][tx]==1){
                visited[ty][tx]=1;
                ans+=1;
                q.push({ty,tx});
            }
        }
    } 
    return ans;
}
int main(void){
    cin >> N >> M >> K;
    for (int i=0;i<K;i++){
        int tmp_y, tmp_x;
        cin >> tmp_y >> tmp_x;
        arr[tmp_y][tmp_x]=1;
    }

    for(int i=1;i<N+1;i++){
        for(int j=1;j<M+1;j++){
            if(!visited[i][j] &&arr[i][j]==1){
                answer=max(answer,bfs(i,j));
            }
        }
    }

    cout << answer ;
}