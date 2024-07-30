#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(void){
    // 4 7 
    // 20 15 10 17
    long long N, M;
    cin >> N >> M;
    long long trees[N];
    for (int i=0;i<N;i++){
        cin >> trees[i];
    }
    long long answer=0;
    long long left = 1;
    long long right = *max_element(trees, trees+N);
    while(left <=right){
        long long point=0;
        long long mid = (left+right)/2;
        //cout << "mid" << mid << endl;
        for (long long i=0;i<N;i++){
            if (trees[i]>mid){
                point+=trees[i]-mid;
            }
        }
        //cout << "point" << point << endl;
        if(point>=M){
            left = mid+1;
            answer=mid;
        }
        else{
            right=mid-1;
        }
    }
    cout << answer;
}