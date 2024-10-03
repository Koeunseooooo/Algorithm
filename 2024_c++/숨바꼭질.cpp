#include <iostream>
// #include <vector>
#include <queue>
#include <stack>
#define MAX 100001
using namespace std;

int N,K;
int cnt;
int min_time=MAX;
int visit[MAX];

void bfs(int n, int time){
    queue<pair<int,int>> q;
    q.push({n,time}); //현재 수빈이의 위치, 시간
    while(!q.empty()){
        int cur_n = q.front().first;
        int cur_time = q.front().second;
        q.pop();

        visit[cur_n]=true;

        if(cur_n==K){
            if(min_time>=cur_time){
                min_time=cur_time; // 얘는 중복(불필요) 계산 되긴 함
                cnt++;
            }
            continue;
        }

        if(cur_n+1 < MAX && cur_n+1 >= 0 && !visit[cur_n+1]){
            // 걷기 +1
            // 범위 체크 후 다음 점이 방문 된 점인지 확인
            q.push(make_pair(cur_n + 1, cur_time + 1)); 
        }
        if(cur_n-1 < MAX && cur_n-1 >= 0 && !visit[cur_n-1]){
            // 걷기 -1
            q.push(make_pair(cur_n - 1, cur_time + 1));
        }
        if(cur_n*2 < MAX && cur_n*2 >= 0 && !visit[cur_n*2]){
            // 순간이동 *2
            q.push(make_pair(cur_n * 2, cur_time + 1));
        }

    }
}

int main(){
    cin >> N >> K;
    bfs(N,0);
    cout << min_time << endl;
    cout << cnt << endl;
}