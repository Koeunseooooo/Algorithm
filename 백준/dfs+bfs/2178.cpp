#include <bits/stdc++.h>

using namespace std;

int N, M;
int maze[101][101];
int visited[101][101];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({y, x});
    visited[y][x] = 1; // 처음 방문 처리

    while(!q.empty()) {
        int cur_y = q.front().first;
        int cur_x = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int next_y = cur_y + dy[i];
            int next_x = cur_x + dx[i];

            if (next_y < 0 || next_y >= N || next_x < 0 || next_x >= M) continue;
            if (maze[next_y][next_x] == 0 || visited[next_y][next_x]) continue;

            q.push({next_y, next_x});
            visited[next_y][next_x] = visited[cur_y][cur_x] + 1;
        }
    }

    return visited[N-1][M-1];
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%1d", &maze[i][j]);
        }
    }

    cout << bfs(0, 0) << "\n";
    return 0;
}