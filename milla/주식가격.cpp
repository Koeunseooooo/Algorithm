#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    
    for(int i=0;i<prices.size();i++){
        int target = prices[i];
        //stack<int> st;
        int tmp=0;
        for (int j=i+1;j<prices.size();j++){
            tmp++;
            if(prices[j]<target){
                break;
            }
        }
        answer.push_back(tmp);
    }
    
    return answer;
}