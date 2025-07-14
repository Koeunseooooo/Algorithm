#include <bits/stdc++.h>

using namespace std;

int n = 5, k = 3, a[5] = {1, 2, 3, 4, 5};

// 재귀방식
void print(vector<int> b){
    for(int i:b)
        cout << i << " ";
    cout << '\n';
}
void combi(int start, vector<int> b)
{
    if(b.size() ==k){
        print(b);
        // logic
        return;
    }

    for (int i = start + 1; i < n;i++){
        b.push_back(i); // 인덱스 기반으로 뽑기 (요소로 뽑으면 헷갈림)
        combi(i, b);
        b.pop_back();
    }
}


int main(void){
    // 재귀방식
    vector<int> b;
    combi(-1, b);

    // 중첩 for문 방식
    for (int i = 0; i < n;i++){
        for (int j = i + 1; j < n;j++){
            for (int k = j + 1; k < n;k++){
                cout << i << j << k << '\n';
            }
        }
    }
        return 0;
}