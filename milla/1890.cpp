// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;
// // 4
// // 2 3 3 1
// // 1 2 1 3
// // 1 2 3 1
// // 3 1 1 0

// vector<vector<int>> arr;
// vector<vector<int>> dp;
// int N;

// void print_dp(){
//     for (int i=0;i<N;i++){
//         for (int j=0;j<N;j++){
//             cout << dp[i][j];
//         }
//         cout << endl;
//     }
//     cout << "---" << endl;;
// }

// bool isValid(int i,int j){ // 세로, 가로, 이동
//     return (i>=0 && i<N && j>=0 && j<N) ? true : false;
// }
// int main(void){
    
//     cin >> N;

//     //m*n인 2차원 벡터를 0으로 초기화하여 선언
//     //vector <vector<int>> v(m, vector<int>(n, 0));

//     //fill(dp, dp+N, MAX_INF); 배열 초기화
//     //fill(arr.begin(),arr.end(),vector<int>(N,0)); // 벡터 초기화

//     fill(dp.begin(),dp.end(),vector<int>(N,0)); // 벡터 초기화
//     arr.resize(N, vector<int>(N));
//     dp.resize(N, vector<int>(N, 0));

    
//     // int arr[N];
//     for (int i=0;i<N;i++){
//         for(int j=0;j<N;j++){
//             // int tmp;
//             // cin >> tmp;
//             // arr[i].push_back(tmp);
//             cin >> arr[i][j];
//         }
        
//     }

//     // for (int i=0;i<N;i++){
//     //     for (int j=0;j<N;j++){
//     //         cout << arr[i][j];
//     //     }
//     // }

    

//     for (int i=0;i<N;i++){
//         for (int j=0;j<N;j++){
//             if(i==N-1 && j==N-1){
//                 break;
//             }
//             int move=arr[i][j];
//             int ny = i + move; // 세로
//             int nx = j + move; // 가로
//             if (isValid(ny,j)){ // 아래쪽
//                 dp[ny][j]+=dp[i][j];
//             }
//             if (isValid(i,nx)){ // 오른쪽
//                 dp[i][nx]+=dp[i][j];
//             }
//             // cout << "idx:" << i*N+(j+1) << endl;
//             // print_dp();
            
//         }
        
//     }
//     cout << dp[N-1][N-1];
    
// } // 반례가 무엇인지 모르겠음.


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 4
// 2 3 3 1
// 1 2 1 3
// 1 2 3 1
// 3 1 1 0

vector<vector<int>> arr;
vector<vector<int>> dp;
int N;

void print_dp(){
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            cout << dp[i][j];
        }
        cout << endl;
    }
    cout << "---" << endl;;
}

bool isValid(int i,int j){ // 세로, 가로, 이동
    return (i>=0 && i<N && j>=0 && j<N) ? true : false;
}
int main(void){
    
    cin >> N;

    //m*n인 2차원 벡터를 0으로 초기화하여 선언
    //vector <vector<int>> v(m, vector<int>(n, 0));

    //fill(dp, dp+N, MAX_INF); 배열 초기화
    //fill(arr.begin(),arr.end(),vector<int>(N,0)); // 벡터 초기화

    fill(dp.begin(),dp.end(),vector<int>(N,0)); // 벡터 초기화
    arr.resize(N, vector<int>(N));
    dp.resize(N, vector<int>(N, 0));

    
    // int arr[N];
    for (int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            // int tmp;
            // cin >> tmp;
            // arr[i].push_back(tmp);
            cin >> arr[i][j];
        }
        
    }

    // for (int i=0;i<N;i++){
    //     for (int j=0;j<N;j++){
    //         cout << arr[i][j];
    //     }
    // }

    
    dp[0][0]=1;
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if(arr[i][j]==0){
                continue;
            }

            if(dp[i][j]!=0){
                int move=arr[i][j];
                int ny = i + move; // 세로
                int nx = j + move; // 가로
                if (isValid(ny,j)){ // 아래쪽
                    dp[ny][j]+=dp[i][j];
                }
                if (isValid(i,nx)){ // 오른쪽
                    dp[i][nx]+=dp[i][j];
                }
                // cout << "idx:" << i*N+(j+1) << endl;
                // print_dp();
            }
        }
    }
    cout << dp[N-1][N-1];
    
} // 반례가 무엇인지 모르겠음.