#include <bits/stdc++.h>

using namespace std;

int M, N, H;
int boxes[100][100][100];
int visited[100][100][100];
int dy[6] = {-1, 0, 1, 0, 0, 0};
int dx[6] = {0, 1, 0, -1, 0, 0};
int dz[6] = {0, 0, 0, 0, -1, 1};

void printBoxes(){
    cout << "--------------------" << endl;
    for (int k = 0; k < H;k++){
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++)
            {
                cout << boxes[k][i][j] << " ";
            }
            cout << endl;
        }
        cout << "--------------------" << endl;
    }
}
void printVisited(){
    cout << "--------------------"<< endl;
    for (int k = 0; k < H;k++){
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++)
            {
                cout << visited[k][i][j] << " ";
            }
            cout << endl;
        }
       
    }
    cout << "--------------------"<< endl;
}

void bfs(queue<tuple<int,int,int>> q){

    while(!q.empty()){
        tuple<int, int, int> cur = q.front();
        int h = get<0>(cur);
        int n = get<1>(cur);
        int m = get<2>(cur);

        q.pop();

        for (int i = 0; i < 6;i++){
            int nz = h + dz[i];
            int ny = n + dy[i];
            int nx = m + dx[i];
            if(nz<0 || nz >=H || ny<0 || ny >=N || nx<0 || nx >=M){
                continue;
            }
            if(boxes[nz][ny][nx]!=0){
                continue;
            }
            boxes[nz][ny][nx] = 1;
            visited[nz][ny][nx] = visited[h][n][m] + 1;
            q.push({nz, ny, nx});
        }

        // printVisited();
    }
}

int main()
{
    cin >> M >> N >> H;

    fill(&boxes[0][0][0], &boxes[0][0][0] + 100 * 100 * 100, 2);
    for (int k = 0; k < H; k++)
    {
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++)
            {
                cin >> boxes[k][i][j];
            }
        }
    }

    queue<tuple<int, int, int>> q;

    for (int k = 0; k < H; k++)
    {
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++)
            {
                if(boxes[k][i][j]==1 && !visited[k][i][j]){
                    q.push({k, i, j});
                    visited[k][i][j] = 1;
                }
            }
        }
    } // 최초로 먼저 담기

    bfs(q);

    int answer = 0;
    for (int k = 0; k < H; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++) {
                if (boxes[k][i][j] == 0 && visited[k][i][j]==0) {
                    cout << -1 << endl;
                    return 0;
                }
                answer = max(answer, visited[k][i][j]);
            }
    cout << answer - 1 << endl; // 시작점이 1이므로 -1
}



