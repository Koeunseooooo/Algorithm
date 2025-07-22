#include <bits/stdc++.h>

using namespace std;

int N;
int target_x, target_y;
int M;
vector<int> nodes[100];
int visited[100]; // 전역 변수는 자동으로 0으로 초기화됨
int res;

void bfs(int target_x, int taget_y)
{
    queue<int> q;
    visited[target_x] = 1;
    q.push(target_x);

    while (!q.empty())
    {
        int cur = q.front();
        q.pop();

        for(int next:nodes[cur]){
            if (!visited[next])
            {
                visited[next] = visited[cur]+1;
                if(next==target_y){
                    res = visited[next]-1;
                    return;
                }
                else{
                    q.push(next);
                }
            }
        }
    }
}

int main()
{
    cin >> N;
    cin >> target_x >> target_y;
    cin >> M;
    for (int i = 0; i < M;i++){
        int temp_x, temp_y;
        cin >> temp_x >> temp_y;
        nodes[temp_x].push_back(temp_y);
        nodes[temp_y].push_back(temp_x);
    }

    bfs(target_x, target_y);
    if(res==0){
        cout << -1 << endl;
    }
    else{
        cout << res << endl;
    }
}