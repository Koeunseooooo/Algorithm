/*
백준 실버4 ATM
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }

    sort(arr.begin(),arr.end());
    // for(int i=0;i<n;i++){
    //     cout << arr[i];
    // }

    int sum=0;
    int prev_sum;
    for(int i=0;i<n;i++){
        sum += arr[i]*(n-i);
        // int temp_sum=prev_sum;
        // temp_sum+=arr[i];
        // //cout << "temp_sum" << temp_sum;
        // sum+=temp_sum;
        // prev_sum=temp_sum;

    }

    cout << sum;
}
