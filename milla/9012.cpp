#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        string str;
        cin >> str;
        stack<char> s;
        string answer ="YES"; // init
        for(int i=0; i<str.length();i++){
            if (str[i] == '(') {
				s.push(str[i]);
			}
            else if (!s.empty() && str[i] == ')' && s.top() == '(') {
				s.pop();
			}
            else{
                answer = "NO";
				break;
            }
        }
        if(!s.empty()){
            answer ="NO";
        }

        cout << answer << endl;
        
    }
}