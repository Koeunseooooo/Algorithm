// 13
// BJBBJOOOJJJJB

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 1000
#define MAX_INF int(1e9)

using namespace std;

char find_target(char target){
    if (target=='B'){
        return 'J';
    }
    else if (target=='O'){
        return 'B';
    }
    else if (target=='J'){
        return 'O';
    }
}
int main(void){
    int N;
    string str;
    cin >> N;
    cin.ignore(); //주의
    getline(cin,str);
    //cout << MAX_INF << endl;
    int dp[MAX];
    fill(dp, dp+N, MAX_INF); // memset과 차이점이 뭐지?
    dp[0]=0;
    for (int i=1;i<N;i++){
        char target=str[i];
        char prev = find_target(target);
        //cout << target << prev << endl;
        for(int j=0;j<i;j++){
            if(str[j]==prev){
                dp[i]=min(dp[i],dp[j]+(i-j)*(i-j));
                //cout << dp[i] << "hello";
            }
        }
        // print_dp();
        // for(int k=0;k<N;k++){
        //     cout << dp[k];
        // }
        //cout << "---" << endl;
    }
    if (dp[N-1]==MAX_INF){
        cout << -1;
    }else{
        cout << dp[N-1];
    }
}