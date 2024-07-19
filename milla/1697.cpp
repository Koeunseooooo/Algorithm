#include <iostream>
#include <cstring>
#include <queue>
#define MAX 1000001

using namespace std;

bool visited[MAX];
int N,K;
queue<pair<int,int>> q;

bool isValid(int x){
    return (x>=0 && x<MAX && !visited[x] ? true : false);
}

void bfs(int n,int init_time){
    q.push({n,init_time});
    visited[n]=1;
    while(!q.empty()){
        int x = q.front().first;
        int time = q.front().second;
        q.pop();
        if(x==K){
            cout << time;
            return;
        }
        if(isValid(x-1)) {
            visited[x-1]=true;
            q.push({x-1,time+1});
        }
        if(isValid(x+1)) {
            visited[x+1]=true;
            q.push({x+1,time+1});
        }
        if(isValid(x*2)) {
            visited[x<<1]=true;
            q.push({x<<1,time+1});
        }
    }

}


int main(void){
    cin >> N >> K;
    memset(visited,0,sizeof(visited));
    bfs(N,0);

}
// #include <iostream>
// #include <vector>
// #define MAX 100000
// using namespace std;
// int N,K;
// int minTime=MAX; // 최솟값 업데이트

// bool isValid(int x){
//     return x>=0 && x <=MAX ? true: false;
// }
// void dfs(int n, int cnt){
//     if(n==K && cnt < minTime){
//         minTime = cnt;
//         return;
//     }
//     if(cnt+1 < minTime){
//         if (isValid(n+1)) dfs(n+1,cnt+1);
//         if (isValid(n-1)) dfs(n-1,cnt+1);
//         if (isValid(n<<1)) dfs(n*2,cnt+1);
//     }
//     // 틀린이유(시간초과) : 코너케이스 (0,10만과 같은 상황 일때) ex. N=1, K=0;
// }

// int main(void){
//     cin >> N >> K;
//     dfs(N,0);
//     cout << minTime << endl;
// }


// void dfs(int n, int cnt){
//     if(n==k){
//         cout << cnt << endl;
//         return;
//     }
//     if(n>k){
//         return;
//     }
//     dfs(n+1,CNT+1);
//     dfs(n-1,CNT+1);
//     dfs(n*2,CNT+1);
// }

// int main(void){
//     cin >> N >> K;
//     dfs(N,K);
// }

// 최솟값 업데이트와 조건 처리
// dfs는 재귀종료조건을 명확하게 짜야한다. 