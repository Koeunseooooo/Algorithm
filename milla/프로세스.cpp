#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> q; //idx,prio
    priority_queue<int> pq; //prio
    
    for(int i=0;i<priorities.size();i++){
        pq.push(priorities[i]);
        q.push({i, priorities[i]});
    }
    
    while(!q.empty()){
        int tar_idx = q.front().first;
        int tar_value = q.front().second;
        // cout << "tar_idx, tar_value; " << tar_idx << tar_value << endl;
        int tar_prio = pq.top();
        // cout << "tar_prio: " << tar_prio << endl;
        
        if(tar_prio>tar_value){
            q.pop();
            q.push({tar_idx, tar_value});
        }
        else{
            q.pop();
            pq.pop();
            answer++;
            if(tar_idx==location){
                break;
            }
        }
        
    }
    
    return answer;
}