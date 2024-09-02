// 해당 문제의 핵심 : 순간 이동(0초)과 걷는 이동(1초)는 우선 순위가 다르다. 
// 따라서 해당 문제는 단순한 bfs를 요구하는 문제가 아니라 bfs는 모든 간선의 가중치가 동일해야 한다는 전제 조건이 필요하다

// 1. 덱방식 + 방문여부 표시를 1/0으로 하지 않고 현재 시간을 입력하여 정보를 단일화함
#include <iostream>
#include <deque>
#include <stdio.h>
#include <cstring> // memset
 
using namespace std;
 
#define MAX_SIZE 100000+1
 
int N, K;
int visited[MAX_SIZE];
 
int bfs() {
    deque<int> dq;
    dq.push_back(N);
    visited[N] = 1;
    while (!dq.empty()) {
         // 덱의 앞의 요소들부터 꺼내옴
        int pos_x = dq.front();
        dq.pop_front();
 
        if(pos_x == K) return visited[K] - 1;
 
        // 순간이동은 덱의 앞쪽에 집어넣음.
        if (pos_x * 2 < MAX_SIZE && !visited[pos_x * 2]) {
            dq.push_front(pos_x * 2);
            visited[pos_x * 2] = visited[pos_x];
        }
 
        // 걷는이동은 덱의 뒤쪽에 집어넣음.
        if (pos_x + 1 < MAX_SIZE && !visited[pos_x + 1]) {
            dq.push_back(pos_x + 1);
            visited[pos_x + 1] = visited[pos_x] + 1;
        }
 
        // 걷는이동은 덱의 뒤쪽에 집어넣음.
        if (pos_x - 1 >= 0 && !visited[pos_x - 1]) {
            dq.push_back(pos_x - 1);
            visited[pos_x - 1] = visited[pos_x] + 1;
        }
    }
}
 
int main() {
    scanf("%d %d", &N, &K);
    printf("%d\n", bfs());
    return 0;
}

// 2. 우선순위큐 활용 (어떻게 쓰는 건지 감이 잘 안온다.. 함수 톺아보자)
#include <iostream>
#include <queue>
#include <stdio.h>
#include <cstring> // memset
 
using namespace std;
 
#define MAX_SIZE 100000+1
 
int N, K;
bool visited[MAX_SIZE];
 
int bfs() {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push({ 0, N });
    visited[N] = true;
    while (!q.empty()) {
        int time = q.top().first;
        int x = q.top().second;
        q.pop();
 
        if (x == K) return time;
 
        if (x * 2 < MAX_SIZE && !visited[x * 2]) {
            q.push({ time, x * 2 });
            visited[x * 2] = true;
        }
 
        if (x + 1 < MAX_SIZE && !visited[x + 1]) {
            q.push({ time + 1, x + 1 });
            visited[x + 1] = true;
        }
 
        if (x - 1 >= 0 && !visited[x - 1]) {
            q.push({ time + 1 , x - 1 });
            visited[x - 1] = true;
        }
    }
}
 
int main() {
    scanf("%d %d", &N, &K);
    printf("%d\n", bfs());
    return 0;
}