#include <string>
#include <vector>
#include <queue>
 
using namespace std;
 
int main(void){
    int bridge_length=2;
    int weight=2;
    vector<int> v = (7,4,5,6);
    solution(bridge_length,weight,v);
}
int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int idx = 0;     // truck_weights의 idx 포인터
    int cur_sum = 0;     // 다리를 건너는 트럭 무게합
    queue<int> q;   // 다리 위에 있는 트럭
 
    for (int i = 0; i < bridge_length; i++)
        q.push(0);
 
    while (!q.empty()) {
        answer++;
        cur_sum -= q.front();
        q.pop();
 
        // 대기 트럭이 있는 경우
        if (idx < truck_weights.size()) {
            if (cur_sum + truck_weights[idx] <= weight) {
                cur_sum += truck_weights[idx];
                q.push(truck_weights[idx]);
                idx++;
            }
            else {
                q.push(0);
            }
        }
        
    }
 
    return answer;
}

