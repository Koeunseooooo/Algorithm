#include <bits/stdc++.h>


using namespace std;

int N, M, V;
bool visited[1002];
vector<int> nodes[10002];
vector<int> dfs_res;
vector<int> bfs_res;

void dfs(int node){
    visited[node] = 1; // 방문 처리
    dfs_res.push_back(node); // 출력 벡터에 추가
    for (int i = 0; i < nodes[node].size(); i++)
    {
        if(!visited[nodes[node][i]]){
            dfs(nodes[node][i]);
        }
    }
}

void bfs(int node){
    queue<int> q;

    q.push(node);
    visited[node] = 1;
    bfs_res.push_back(node);

    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for (int i = 0; i < nodes[cur].size(); i++) {
            int next = nodes[cur][i];
            if (!visited[next]) {
                q.push(next);
                visited[next] = 1;
                bfs_res.push_back(next);
            }
        }
    }
}

int main()
{
    cin >> N >> M >> V;

    for (int i = 0; i < M;i++){
        int first_n, final_n;
        cin >> first_n >> final_n;
        nodes[first_n].push_back(final_n); // 양방향 간선정리
        nodes[final_n].push_back(first_n);
    }

    for (int i = 1; i < M;i++){
        sort(nodes[i].begin(), nodes[i].end());
    }

    dfs(V); // 1번째 정점부터 방문 시작
    for (int i = 0; i < dfs_res.size();i++){
        cout << dfs_res[i] << " ";
    }

    // visited 초기화
    fill(visited, visited + 1002, 0);

    cout << "\n";
    bfs(V); // 1번째 정점부터 방문 시작
    for (int i = 0; i < bfs_res.size();i++){
        cout << bfs_res[i] << " ";
    }
}
