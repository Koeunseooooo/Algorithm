#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

// struct VS{
//   int home, away;
// };

int result[6][3], madeResult[6][3];
vector<pair<int,int>> vs;

int dfs(int played){
  if(played == 15){
    for(int i = 0; i < 6; i++){
      for(int j = 0; j < 3; j++){
        if(result[i][j] != madeResult[i][j]) return 0;
      }
    }
    return 1;
  }

  int ans = 0;
  int home = vs[played].first;
  int away = vs[played].second;
  //승패
  madeResult[home][0]++; madeResult[away][2]++;
  ans = max(ans,dfs(played + 1));
  madeResult[home][0]--; madeResult[away][2]--;

  //패승
  madeResult[away][0]++; madeResult[home][2]++;
  ans = max(ans,dfs(played + 1));
  madeResult[away][0]--; madeResult[home][2]--;

  //무무
  madeResult[away][1]++; madeResult[home][1]++;
  ans = max(ans,dfs(played + 1));
  madeResult[away][1]--; madeResult[home][1]--;

  return ans;
}

int main(){
  for(int i = 0; i < 6; i++){
    for(int j = i + 1; j < 6; j++){
      vs.push_back({i,j});
    }
  }
  for(int t = 0; t < 4; t++){ //테스트케이스 4로 고정
    memset(madeResult,0,sizeof(madeResult));
    for(int i = 0; i < 6; i++){
      for(int j = 0; j < 3; j++){
        cin >> result[i][j];
      }
    }
    cout << dfs(0) << ' ';
  }
}