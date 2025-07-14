#include <bits/stdc++.h>

using namespace std;

const int max_size =104;
int n;
int a[max_size][max_size];
int visited[max_size][max_size];
int max_len;
int dy[] = {-1,0,1,0};
int dx[] = {0, -1, 0, 1};
int ret=1;

void printMap(int lvl){
    cout << "=========printMap=======\n";
    cout << "=========lvl" << lvl <<"======\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n;j++){
            cout << visited[i][j] << ' ';
        }
        cout << '\n';
    }
    return;
}

void dfs(int y, int x, int lvl){
    visited[y][x] = 1;
    for (int i = 0; i < 4;i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(ny<0 || nx<0 || nx>=n || ny>=n){
            continue;
        }
        if(a[ny][nx]>lvl && !visited[ny][nx]){
            dfs(ny, nx, lvl);
        }
    }
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin >> n;
    for (int i = 0; i < n;i++){
        for (int j = 0; j < n;j++){
            cin >> a[i][j];
            max_len = max(max_len, a[i][j]);
        }
    }

    for (int lvl = 1; lvl < max_len; lvl++)
    {
        fill(&visited[0][0], &visited[0][0] + max_size * max_size, 0);
        int cnt=0;
        for (int j = 0; j < n;j++){
            
            for (int k = 0; k < n; k++)
            {
                if(a[j][k]>lvl && !visited[j][k]){
                    dfs(j, k, lvl);
                    cnt++;
                    
                }
            }
            
        }
        // printMap(lvl);
        // cout << "cnt: " << cnt << '\n';
        ret = max(ret, cnt);
    }
    cout << ret << '\n';
}