#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    priority_queue<int> pq_max;
    priority_queue<int,vector<int>,greater<int>> pq_min;
    
    int cnt = 0;
    for(int i=0;i<operations.size();i++){
        string tmp = operations[i];
        string tmp_oper;
        int tmp_value;

        stringstream ss(tmp);

        // 띄어쓰기를 기준으로 각 값을 변수에 담기
        ss >> tmp_oper >> tmp_value;
        
        if(cnt==0){
            while(!pq_max.empty()){
                pq_max.pop();
            }
            while(!pq_min.empty()){
                pq_min.pop();
            }
        }
        if(tmp_oper=="I"){
            pq_max.push(tmp_value);
            pq_min.push(tmp_value);
            cnt++;
        }
        else{
            if(tmp_oper=="D"){
                if (tmp_value==1 && cnt!=0){
                    pq_max.pop();
                    cnt--;
                }
                else if (tmp_value == -1 && cnt!=0){
                    pq_min.pop();
                    cnt--;
                }
            }
            
        }
    }
    //if(pq_min.empty() && pq_max.empty()){ // 남아 있을 수 있음 (예시:테스트1)
    if(cnt==0){ 
        answer.push_back(0);
        answer.push_back(0);
    }
    else{
        answer.push_back(pq_max.top());
        answer.push_back(pq_min.top());
    }
    
    return answer;
}