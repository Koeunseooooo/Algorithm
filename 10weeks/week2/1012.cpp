#include <bits/stdc++.h>

using namespace std;

int t;
int n, m, k;
int x, y;
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, -1, 0, 1};
int arr[54][54];
int visited[54][54];

void dfs(int y, int x){
    visited[y][x] = 1;

    for (int i = 0; i < 4; i++)
    {
        int ny = y+dy[i];
        int nx = x + dx[i];
        if(ny<0 || nx<0 || ny>=n || nx>=m){
            continue;
        }
        if(arr[ny][nx]==1 && !visited[ny][nx]){
            dfs(ny, nx);
        }
    }
    return;
}

int main(){
    // n이 y
    ios_base::sync_with_stdio(false);

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        // int arr[54][54]={};
        // scanf("%d %d %d", &m, &n, &k);
        cin >> m >> n >> k;
        fill(&arr[0][0], &arr[0][0] + 54 * 54, 0);
        fill(&visited[0][0], &visited[0][0] + 54 * 54, 0);
        for (int i = 0; i < k; i++)
        {
            int a, b; // b기 y
            cin >> a >> b;
            arr[b][a] = 1;
        }
        // for (int i = 0; i < n; i++){
        //     for (int j = 0; j < m;j++){
        //         printf("%d ", arr[i][j]);
        //     }
        //     printf("\n");
        // }
        int res=0;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m;j++){
                if(arr[i][j]==1 && !visited[i][j]){
                    dfs(i, j);
                    res++;
                }
            }
        }
        cout << res << '\n';
    }

    
}