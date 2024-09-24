#include <string>
#include <vector> 
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;


struct cmp {
    bool operator()(const pair<int,int> &a, const pair<int,int> &b){
        return a.second > b.second; // 오름차순(우선순위힙은 swap을 기준으로 비교하는 구문이기에 부등호 주의해야 함)
    }
};

struct cmp{
    bool operater()(const pair<int,int> &a, const pair<int,int> &b){
        return a.second < b.second; // 오름차순
    }
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    // 요청 시간 기준으로 정렬 (기본적으로는 요청 시점이 빠른 순으로 정렬해야함)
    sort(jobs.begin(),jobs.end());
    
    // for(int i=0;i<jobs.size();i++){
    //     // cout << jobs[i];
    //     for(int j=0;j<jobs[i].size();j++){
    //         cout << jobs[i][j];
    //     }
    //     cout << endl;
    // }
    
    priority_queue<pair<int,int>,vector<pair<int,int>>, cmp> pq;
    int currTime=0;
    int i=0;
    int jobSize = jobs.size();
    
    while(true){
        if(i>=jobSize && pq.empty()){
            break;
        }
        
        while(i<jobSize && jobs[i][0]<=currTime){
            pq.push({jobs[i][0],jobs[i][1]});
            i++;
        }
        
        if (!pq.empty()){
            answer+= (currTime+pq.top().second -pq.top().first);
            currTime+=pq.top().second;
            pq.pop();
        } else{
            currTime = jobs[i][0];
        }
    }
    answer /=jobSize;
    return answer;
}