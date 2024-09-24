#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    priority_queue<int> pq_max;
    priority_queue<int,vector<int>,greater<int> pq_min;
    
    
    for(int i=0;i<operations.size();i++){
        string tmp = operations[i];
        string tmp_oper;
        int tmp_value;

        stringstream ss(tmp);

        // 띄어쓰기를 기준으로 각 값을 변수에 담기
        ss >> tmp_oper >> tmp_value;
        
        if(tmp_oper=='I'){
            pq_max.push(tmp_value);
            pq_min.push(tmp_value);
        }
        else{
            if(pq_max.empty() && pq_min.empty()){
                continue
            }
            if(tmp_oper=="D"){
                if (tmp_value==1){
                    pq_max.pop();
                }
                else if (tmp_value == -1){
                    pq_min.pop();
                }
            }
            if(pq_max.empty() || pq_min.empty()){
                while(!pq_max.empty()){
                    pq_max.pop();
                }
                while(!pq_min.empty()){
                    pq_min.pop();
                }
            }
        }
    }
    if(pq_min.empty() && pq_max.empty()){
        answer.push(0);
        answer.push(0);
    }
    else{
        answer.push(pq_max.pop());
        answer.push(qp_min.pop());
    }
    
    return answer;
}