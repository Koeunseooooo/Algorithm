#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int sum = brown+yellow;
    for(int i=3;i<sum;i++){
        if(sum%i==0){
            int width = sum/i;
            int height = i;
            if(width>=3 and height<=width){ //가로>=세로
                int yellow_sum = (width-2)*(height-2);
                if (yellow_sum==yellow){
                    answer.push_back(width);
                    answer.push_back(height);
                }
            }
        }
    }
    return answer;
}