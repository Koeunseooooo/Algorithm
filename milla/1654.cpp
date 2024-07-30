#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int K, N; // 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
    cin >> K >> N;
    long long cables[N];
    for (int i=0;i<K;i++){
        cin >> cables[i];
    }
    // for (int i=0;i<K;i++){
    //     cout << cables[i] << endl;
    // }
    sort(cables,cables+K);
    long long left = 1;
    long long right = cables[K-1];
    long long answer=0;

    while (left<=right){
        long long mid = (left+right)/2; // 랜선의 길이
        //cout << "mid" << mid << endl;
        long long tmp=0;
        for(int i=0;i<K;i++){
            tmp+=(cables[i]/mid);
        }
        //cout << "tmp" << tmp << endl;
        if (tmp>=N){
            answer=mid;
            left = mid +1;
        }
        else{
            right = mid -1;
        }
        //cout << "answer" << answer << endl;

    }
    cout << answer;


}