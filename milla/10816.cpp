#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
    int N;
    cin >> N;
    vector<int> arr(N);
    // 단순 배열의 정렬은 어떻게 하는거지?
    for (int i=0;i<N;i++){
        cin >> arr[i];
    }

    sort(arr.begin(),arr.end());

    int M;
    cin >> M;
    vector<int> find(N);
    for (int i=0;i<M;i++){
        cin >> find[i];
    }
    
    // for (int i=0;i<N;i++){
    //     cout << arr[i] << ' ';
    // }
    // cout << endl;

    for (int i=0;i<M;i++){
        int result = upper_bound(arr.begin(),arr.end(),find[i])-lower_bound(arr.begin(),arr.end(),find[i]);
        
        if (i==M-1){
            cout << result;
        }
        else{
            cout << result << ' ';
        }
    }

}