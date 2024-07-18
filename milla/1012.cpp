#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#define MAX 51

using namespace std;
 
int N, M, k; // 세로, 가로
bool arr[MAX][MAX];
bool visited[MAX][MAX];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
queue<pair<int,int>> q;

void bfs(int n, int m){ // 세로, 가로
    q.push({n,m});
    while(!q.empty()){
        int t_y = q.front().first;
        int t_x = q.front().second;
        q.pop();
        visited[t_y][t_x]=1;
        for(int i=0;i<4;i++){
            int ny = t_y + dy[i];
            int nx = t_x + dx[i];
            if(ny>=0 && ny<N && nx>=0 && nx<M && arr[ny][nx] && !visited[ny][nx]) {
                q.push({ny,nx});
                visited[ny][nx]=1;
            }
        }
    }

}

// void bfs(int xx, int yy) {
// 	q.push({ xx, yy });
// 	while (!q.empty()) {
// 		int x = q.front().first;
// 		int y = q.front().second;
// 		q.pop();
// 		visited[x][y] = true;

// 		for (int i = 0; i < 4; i++) {
// 			int nx = x + dx[i];
// 			int ny = y + dy[i];

// 			if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visited[nx][ny] && arr[nx][ny] == 1) {
// 				visited[nx][ny] = true;
// 				q.push({ nx, ny });
// 			}
// 		}
// 	}
// }

void init() {
	while (!q.empty()) q.pop();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = false;
			arr[i][j] = 0;
		}
	}
}

int main(void){
    int t;
    cin >> t;
    for (int i=0;i<t;i++){
        cin >> M >> N >> k; // 가로, 세로
        memset(arr,0,sizeof(arr));
        memset(visited,0,sizeof(visited));
        //init();

        // 양배추 심기
        for (int i=0;i<k;i++){
            int _m, _n;
            cin >> _m >> _n;
            arr[_n][_m]=1;
        }

        int cnt=0;

        // bfs
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (!visited[i][j]&&arr[i][j]==1){
                    bfs(i,j);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
    }
}