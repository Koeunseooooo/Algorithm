#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(void){
    int N;
    cin >> N;
    int arr[N];
    for(int i=0;i<N;i++){
        cin >> arr[i];
    }

    sort(arr,arr+N);

    int M;
    cin >> M;
    int tar[M];
    for(int i=0;i<M;i++){
        cin >> tar[i];
    }
    
    for(int i=0;i<M;i++){
        int result = binary_search(arr,arr+N,tar[i]);
        cout << result << endl;
    }
}