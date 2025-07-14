#include <bits/stdc++.h>

using namespace std;

const int MAX = 104;
int m, n, k;
int arr[MAX][MAX];
int visited[MAX][MAX];
int cnt;
int dy[] = {-1,0,1,0};
int dx[] = {0, -1, 0, 1};
vector<int> widths;

int dfs(int y, int x)
{
    int res = 1;
    visited[y][x] = 1;
    for (int i = 0; i < 4;i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if( ny <0 || nx <0 || ny >=m || nx>=n){
            continue;
        }
        if(!visited[ny][nx] && (arr[ny][nx]==0)){
            res += dfs(ny, nx);
        }
    }

    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> m >> n >> k;
    //m 이 y
    
    for(int i=0;i<k;i++){
        int l_x, l_y, r_x, r_y;
        cin >> l_x >> l_y >> r_x >> r_y;

        for (int i = l_y; i < r_y;i++){
            for (int j = l_x; j < r_x;j++){
                arr[i][j] = 1;
            }
        }
    }

    // printArr(m, n);
    vector<int> res;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n;j++){
            if (arr[i][j] == 0 && !visited[i][j]){
                res.push_back(dfs(i, j));
                cnt++;
                // printVisited(m, n);
            }
        }
    }
    sort(res.begin(), res.end());

    cout << cnt << '\n';
    for (auto ele : res)
    {
        cout << ele << ' ';
    }
    
}