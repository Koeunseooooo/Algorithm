#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <sstream>


using namespace std;

int main(void){
    int n;
    cin >> n;
    cin.ignore(); // 이거 안해주면 For문으로 넘어가질 않음
    for (int i=0; i<n;i++){
        string s;
        getline(cin,s);
        s+=' '; // 공백을 하나 더 넣어주기

        stack<char> st;
        for (int i=0;i<s.length();i++){
            if(s[i]!=' '){
                st.push(s[i]);
            }
            else{
                while(!st.empty()){
                    cout << st.top();
                    st.pop();
                }
                cout << ' ';
            }
        }

    }
}