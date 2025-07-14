#include <bits/stdc++.h>

using namespace std;

string str;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    getline(cin, str);

    for (int i = 0; i < str.size();i++){
        if(str[i] >=65 && str[i] < 97){
            if(str[i]+13 >90){
                str[i] = str[i] + 13 - 26;
            }
            else{
                str[i] = str[i] + 13;
            }
        }
        else if(str[i]>=97 && str[i] <=122){
            if(str[i]+13 >122){
                str[i] = str[i] + 13 - 26;
            }
            else{
                str[i] = str[i] + 13;
            }
        }
        cout << str[i];
    }
}