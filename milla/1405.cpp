#include <iostream>
#include <vector>

// 로봇이 같은 곳을 한 번보다 많이 이동하지 않을 떄 
// = 로봇이 같은 곳에 한 번만 이동할 때

#define MAX 14

using namespace std;

int arr[2*MAX+1][2*MAX+1]={0,}; //0으로 초기화
int prob[4]; // 동, 서, 남, 북
int dx[4] = {1,-1,0,0}; // prob와 동일한 순서로
int dy[4] = {0,0,1,-1};
int N;
int result=0;

bool isValid(int y, int x){
    return (y>=0 && y<(2*MAX)+1 && x>=0 && x<(2*MAX)+1);
}
void dfs(int cur_prob,int cnt, int cur_x, int cur_y){
    if(cnt==N){
        result+=cur_prob;
        return;
    }
    for (int i=0;i<4;i++){
        int nx=cur_x+dx[i];
        int ny=cur_y+dy[i];

        if (arr[ny][nx]){
            continue;
        }
        // if (!isValid(ny,nx)){
        //     continue;
        // }
        arr[ny][nx]=1;
        cout << cur_prob*0.01*prob[i] << "test" << endl;
        dfs(cur_prob*(0.01*prob[i]),cnt+1,nx,ny);
        arr[ny][nx]=0;
    }

}
int main(void){
    cin >> N; // N번의 행동을 취할 것(총 이동 N번! 경우의 수는 다양)
    for (int i=0;i<4;i++){
        cin >> prob[i];
    }

    arr[N][N]=1;
    dfs(1,0,N,N); // cur_prob, cnt(횟수), x,y (배열의 중점에서 시작)
    cout << result;
}