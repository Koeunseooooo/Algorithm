#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n,m,num;
    cin >> n;
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin >> v[i];
    }

    sort(v.begin(),v.end());

    cin >> m;
    for(int i=0;i<m;i++){
        cin >> num;
        if(binary_search(v.begin(),v.end(), num)){
            cout << "1" << "\n";
            // 문제는 endl; endl의 경우 flush() 함수를 겸하기 때문에 실행마다 출력 버퍼를 지워주는 과정(flush)이 생겨
            // "\n" 보다 속도가 느리다. 따라서 시간 초과가 발생할 경우 endl 대신 "\n"으로 바꿔주면 된다.
        }
        else{
            cout << "0" << "\n";
        }
    }
    return 0;
}