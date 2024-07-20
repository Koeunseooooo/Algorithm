// #include <iostream>
// #include <queue>
// #include <vector>
// #include <string>
// #define MAX 101

// using namespace std;
// string arr[MAX];
// int N, M;


// int main (void){
//     cin >> N >> M ; // 세로, 가로;
//     for (int i=0;i<N;i++){
//         string line;
//         cin >> line;
//         arr[i] = line;
//     }
//     for (int i=0;i<N;i++){
//         for (int j=0;j<M;j++){
//             cout << arr[i][j];
//         }
//     }
// }

#include <iostream>
#include <string>
#include <queue>
#define MAX 100

using namespace std;

int arr[MAX][MAX];
int N, M; // 세로, 가로
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};
queue<pair<int,int>> q;

void bfs(int y,int x){
    q.push({y,x});
    arr[y][x]+=1;
    while(!q.empty()){
        int _y=q.front().first;
        int _x=q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int ny = _y + dy[i];
            int nx = _x + dx[i];

            if (ny >=0 && nx >= 0 && ny < N && nx < M && arr[ny][nx]==1){
                if(ny==N-1 && nx==M-1){
                    cout << arr[_y][_x] << endl;
                    return;
                }
                arr[ny][nx]=arr[_y][_x]+1;
                q.push({ny,nx});
            }
        }
    }
}
int main(void){
    cin >> N >> M;
    for (int i=0;i<N;i++){
        string temp;
        cin >> temp;
        for (int j=0;j<M;j++){
            arr[i][j]=temp[j]-'0';
        }
    }
    bfs(0,0);
    // 출력 형태 확인
    // for(int i=0;i<N;i++){
    //     for (int j=0;j<M;j++){
    //         cout << arr[i][j];
    //     }
    // }
}