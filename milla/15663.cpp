// #include <iostream>
// #include <vector>

// using namespace std;

// int N, M;
// vector<int> vec;
// int ans[10];
// bool visit[10];


// void backtracking(int level){
//     if (level==M){
//         for (int i=0;i<10;i++){
//             if(visit[i]) cout << i ;
//         }
//         cout << '\n';
//         // for (int i=0; i<M; i++) cout << vec[i] << ' ';
//         // cout << '\n';
//         return;
//     }else{
//         for(int i = 0; i <= vec.size(); i++){
//             int tar = vec[i];
//             if(visit[tar] == false){
//                 visit[tar] = true;
//                 vec.push_back(tar);
//                 backtracking(level+1);
//                 vec.pop_back();
//                 visit[tar] = false;
//             }
//         }
//     }
// }

// int main(void){
//     cin >> N >> M;
//     for (int i=0;i<N;i++){
//         int temp;
//         cin >> temp;
//         vec.push_back(temp);
//         //origin.push_back(i);
//     }
//     sort(vec.begin(),vec.end());
//     vec.erase(unique(vec.begin(),vec.end()),vec.end());
//     // for (int i=0; i<vec.size(); i++) cout << vec.at(i) << ' ';
//     // cout << '\n';
//     backtracking(0);
// }

#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int input[10];
int ans[10];
bool isUsed[10];

void func(int L){
    if (L == M){
        for (int i=0; i<M; i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }

    int tmp = 0;
    for (int i=0; i<N; i++){
        if (!isUsed[i] && tmp != input[i]){
            ans[L] = input[i];
            tmp = input[i];
            isUsed[i] = true;
            func(L+1);
            isUsed[i] = false;
        }
    }
}

int main(){
    cin >> N >> M;
    for (int i=0; i<N; i++) cin >> input[i];
    sort(input, input+N);
    // for (int i=0; i<N; i++) cout << input[i] << ' ';
    // cout << '\n';
    func(0);

    return 0;
}