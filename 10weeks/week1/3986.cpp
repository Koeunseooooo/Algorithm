#include <bits/stdc++.h>

using namespace std;

int n;
int cnt;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n;i++){
        string str;
        stack<char> st;
        cin >> str;
        for(char ch : str){
            if(st.size() && st.top()==ch){
                st.pop();
            }
            else{
                st.push(ch);
            }
        }
        if(st.size()==0){
            cnt++;
        }
    }
    cout << cnt << '\n';
}