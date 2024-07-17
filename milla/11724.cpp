#include <iostream>
#include <vector>
#include <queue>
#define MAX 1001

using namespace std;
vector<int> vec[MAX];
bool visited[MAX];

void bfs(int x){
    queue<int> q;
    visited[x]=1;
    q.push(x);
    while(!q.empty()){
        int tar = q.front();
        q.pop();
        for(int i=0;i<vec[tar].size();i++){
            if(visited[vec[tar][i]]==0){
                visited[vec[tar][i]]=1;
                q.push(vec[tar][i]);
            }
        }
    }
    
}
int main(void){
    int n, m ;
    int cnt=0;
    cin >> n >> m ;
    for(int i=0;i<m;i++){
        int a, b;
        cin >> a >> b ;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    for (int i=1;i<=n;i++){
        if(visited[i]==0){
            bfs(i);
            cnt++;
        }
    }

    cout << cnt ;
}