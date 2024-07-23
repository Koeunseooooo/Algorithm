#include <iostream>

using namespace std;
int N,M;
int ans[8];
int visited[8];

void bt(int level){
    if(level==M){
        for(int i=0;i<M;i++){
            cout << ans[i] << ' ';
        }
        cout << endl; //possible?
        return ;
    }
    for (int i=1;i<=N;i++){
        //if(!visited[i]){
            visited[i]=1;
            ans[level]=i;
            bt(level+1);
            visited[i]=0;
        //}
    }
}
int main(void){
    cin >> N >> M;
    memset(ans,0,sizeof(ans));
    memset(visited,0,sizeof(visited));
    bt(0);
}