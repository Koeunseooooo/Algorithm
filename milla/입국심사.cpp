#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());
    int left = 1;
    int right = n*times.back();
    while(left <=right){
        int mid = (left+right)/2;
        int pass=0;
        for(int i=0;i<times.size();i++){
            pass += (mid/times[i]);
        }
        if(pass>=n){
            right=mid-1;
            answer=(long long)mid;
        }
        else{
            left=mid+1;
        }
    }
    return answer;
};

int main(void){
    int n=6;
    vector<int> times = {7, 10};
    long long answer1 = solution(n, times);
    cout << answer1;
}