#include <iostream>
#include <queue>
#include <string>

using namespace std;
#define MAX 26

int n, cnt =0;
string arr[MAX];
bool visited[MAX][MAX]={0,};
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
queue<pair<int,int>> q;
vector<int> result;

void bfs(int i,int j){
    
    visited[i][j]=1;
    q.push({i,j}); // 중괄호를 사용
    cnt++;

    while(!q.empty()){
        int a = q.front().first;
        int b = q.front().second;
        q.pop();
        for (int i=0;i<4;i++){
            int nx = a+dx[i];
            int ny = b+dy[i];
            if(0<=nx && nx <n && 0<=ny && ny <n && visited[nx][ny]==0 && arr[nx][ny]=='1'){
                q.push({nx,ny});
                visited[nx][ny]=1;
                cnt++;
            }
        }
    }

}

int main(void){
    
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }

    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            if(arr[i][j]=='1'&&visited[i][j]==0){
                cnt =0;
                bfs(i,j);   
                result.push_back(cnt);
            }
        }
    }

    cout << result.size() << endl;
    for (int i=0;i<result.size();i++){
        cout << result[i] << endl;

    }
} 