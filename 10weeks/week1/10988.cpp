#include <bits/stdc++.h>

using namespace std;

string str;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> str;

    int st = 0;
    int ed = str.length() - 1;

    int res = 1;
    while (st <= ed)
    {
        if(st==ed){
            break;
        }

        if(str[st]==str[ed]){
            st++;
            ed--;
            continue;
        }else{
            res = 0;
            break;
        }
    }

    cout << res;


    // 2. reverse 사용하기
    string temp = str;
    reverse(temp.begin(), temp.end());
    if(temp==str)
        cout << 1 << '\n';
    else{
        cout << 0 << '\n';
    }
}