#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> nodes[101];
vector<int> visited(101, 0);

void dfs(int node)
{
    visited[node] = 1;
    for (int i = 0; i < nodes[node].size(); i++)
    {
        int next_node = nodes[node][i];
        if (!visited[next_node]) {
            dfs(next_node);
        }
    }
}

int main(){
    cin >> N;
    cin >> M;
    for (int i = 0; i < M;i++){
        int temp_a, temp_b;
        cin >> temp_a >> temp_b;
        nodes[temp_a].push_back(temp_b);
        nodes[temp_b].push_back(temp_a);
    }

    dfs(1);

    int cnt = 0;
    for (int i = 2; i <= N;i++){ // 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 = 1제외
        if(visited[i])
            cnt++;
    }

    cout << cnt << endl;
}