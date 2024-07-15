#include <iostream>
#include <vector>
#include <queue>
#define MAX 1001
using namespace std; 

int n, m, v;
int map[MAX][MAX];
bool visited[MAX];
queue<int> q;

void reset(){
    for (int i=1;i<=n;i++){
        visited[i]=0;
    }
}

void DFS(int v){
    visited[v]=1;
    cout << v << " ";
    for (int i=1;i<=n;i++){
        if(map[v][i]==1 && visited[i]==0){
            DFS(i);
        }
    }
}

void BFS(int v){
    q.push(v);
    visited[v] = true;
    cout << v << " ";
    while(!q.empty()){
        v=q.front();
        q.pop();

        for (int i=1;i<=n;i++){
            if(map[v][i]==1 && visited[i]==0){
                q.push(i);
                visited[i]=true;
                cout << i << " ";
            }
        }
    }
}

int main(void){
    cin >> n >> m >> v;

    for (int i=0;i<m;i++){
        int a, b;
        cin >> a >> b;
        map[a][b]=1;
        map[b][a]=1;
    }

    reset();
    DFS(v);

    cout << '\n';

    reset();
    BFS(v);
}