// #include <iostream>
// #include <vector>
// #define MAX 20

// using namespace std;
// int N, M;
// int arr[MAX];
// bool visited[MAX]={0,};
// int ans=0;
// int result=0;

// void dfs(int cur){
//     if (cur ==M){
//         result++;
//         return
//     }
//     for(int i=0;i<N;i++){
//         if (!visited[i]){
//             visited[i]=1;
//             ans+=arr[i];
//             dfs(ans);
//             visite[i]=0;
//             ans-=arr[i];
//         }
//     }



// }

// int main(void){
//     cin >> N >> M;
//     for (int i=0;i<N;i++){
//         int tmp;
//         cin >> tmp;
//         arr[i]=tmp;
//     }
//     dfs();
//     cout << result;
// }

#include <iostream>
#include <vector>
#define MAX 20

using namespace std;
int N, M;
int arr[MAX];
bool visited[MAX]={0,};
int result=0;

void dfs(int level, int cur){
    if (level==N){// 모든 수를 다 더하면 리턴
        return;
    }
    if(arr[level]+cur==M){
        result++;
    }

    dfs(level+1,cur);
    dfs(level+1,cur+arr[level]);
    // for(int i=0;i<N;i++){
    //     if (!visited[i]){
    //         visited[i]=1;
    //         ans+=arr[i];
    //         dfs(ans);
    //         visite[i]=0;
    //         ans-=arr[i];
    //     }
    // }



}

int main(void){
    cin >> N >> M;
    for (int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        arr[i]=tmp;
    }
    dfs(0,0);
    cout << result;
}