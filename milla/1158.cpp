#include <iostream>
#include <queue>

using namespace std;


int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, k;
    cin >> n >> k;
    queue<int> q;
    for(int i=0;i<n;i++){
        q.push(i+1);
    }

    cout << "<";
    while(q.size()>1){
        // q.size()!=0;
        for(int i=0;i<k-1;i++){
            int tar = q.front();
            q.pop(); // 빼고
            q.push(tar); // 뒤에 다시 넣기
        }
        cout << q.front() << ", ";
        q.pop();
    }
    cout << q.front() << ">";
}