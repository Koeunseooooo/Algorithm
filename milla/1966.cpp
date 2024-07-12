#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(void){
    // 문서의 수와 중요도가 주어졌을 때
    // 어떤 한 문서가 몇 면째로 인쇄되는지 알아내야함

    // input 1 : 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서
    // input 2 : 중요도 순

    // best case : 4개의 문서가 있고, 중요도가 2 1 4 3 이라면,

    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int n, tar;
        int order=1;
        int bigger=false;
        cin >> n >> tar;
        queue<int> seq; 
        vector<int> imp(n); // n만큼 크기 지정

        for (int i=0;i<n;i++){
            cin >> imp[i];
            seq.push(i);
        }

        while (!seq.empty()){
            for(int k=1;k<imp.size();k++){
                if(imp[0] < imp[k]){
                    bigger = true;
                    break;
                }
                else{
                    bigger = false;
                }
            }

            if (bigger == true){
                seq.push(seq.front());
                seq.pop();

                imp.push_back(imp[0]);
                imp.erase(imp.begin() + 0 ); // 0의 의미?
            }
            else{
                if(seq.front() == tar){
                    cout << order << '\n';
                    break;
                }
                else{
                    order++;
                    
                    seq.pop();
                    imp.erase(imp.begin() +0);
                }
            }
        }
    }
}

// 다른 풀이 엄청 많을 듯... pair로 작업하는 것 + 우선순위큐로 작업하는 것?? 한 번 찾아볼 것 