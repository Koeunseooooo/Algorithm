#include <bits/stdc++.h>


using namespace std;

int N, M, V;
bool visited[1002];
vector<int> nodes[10002];
vector<int> dfs_res;

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

int main()
{
    cin >> N >> M >> V;

    for (int i = 0; i < M;i++){
        int first_n, final_n;
        cin >> first_n >> final_n;
        nodes[first_n].push_back(final_n); // 양방향 간선정리
        nodes[first_n].push_back(final_n);
    }

    for (int i = 1; i < M;i++){
        sort(nodes[i].begin(), nodes[i].end());
    }

    dfs(1); // 1번째 정점부터 방문 시작
    for (int i = 0; i < dfs_res.size();i++){
        cout << dfs_res[i] << " ";
    }
}
