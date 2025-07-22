#include <bits/stdc++.h>


using namespace std;

int N;
vector<int> houses[26];
vector<vector<int>> visited(26, vector<int>(26, 0));
int ny[4] = {-1, 0, 1, 0};
int nx[4] = {0, 1, 0, -1};
int cnt = 0;

void dfs(int y, int x)
{
    visited[y][x] = 1;
    cnt++;
    for (int i = 0; i < 4; i++)
    {
        int new_y = y + ny[i];
        int new_x = x + nx[i];

        if (new_y < 0 || new_y >= N || new_x <0 || new_x >= N){
            continue;
        };
        if(visited[new_y][new_x]!=0 || houses[new_y][new_x]==0){
            continue;
        }
        dfs(new_y, new_x);
    }
}

void printHouse() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << houses[i][j];
        }
        cout << '\n';
    }
}

//printVisited function to print the visited matrix
void printVisited() {
    cout << "------------------\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << visited[i][j];
        }
        cout << '\n';
    }
    cout << "------------------\n";
}
int main()
{
    cin >> N;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        // for (char c : s) {
        //     houses[i].push_back(c - '0');
        // }
        for(int j = 0; j < N; j++) {
            houses[i].push_back(s[j] - '0');
        }
    }

    vector<int> res;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j] && houses[i][j] == 1) {
                cnt = 0;
                dfs(i, j);
                res.push_back(cnt);
                // printVisited();
            }
        }
    }
    cout << res.size() << '\n';
    sort(res.begin(), res.end());
    for (int x : res) cout << x << '\n';
}