#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main(void){
    int N;
    cin >> N;
    vector<int> v(N);
    //int copy_arr[N];
    
    
    for(int i=0;i<N;i++){
        cin >> v[i];
    }
    vector<int> copy_arr(v);
    // copy(arr,arr+N,copy_arr);
    // for(int i=0;i<N;i++){
    //     cout << copy_arr[i];
    // }
    sort(copy_arr.begin(), copy_arr.end());
    copy_arr.erase(unique(copy_arr.begin(),copy_arr.end()),copy_arr.end());
    // for(int i=0;i<copy_arr.size();i++){
    //     cout << copy_arr[i];
    // }

    for(int i=0;i<N;i++){
        cout << lower_bound(copy_arr.begin(),copy_arr.end(),v[i])-copy_arr.begin() << ' ';
    }
    
}