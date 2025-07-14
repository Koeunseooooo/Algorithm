#include <bits/stdc++.h>

using namespace std;

int num;
int cnt[26];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> num;
    for (int i = 0; i < num;i++){
        string temp;
        cin >> temp;

        cnt[temp[0] - 'a']++;
    }

    int flag = 0;
    for (int i = 0; i < 26; i++)
    {
        if(cnt[i]>=5){
            flag = 1;
            cout << char(97 + i);
        }
    }

    if(!flag){
        cout << "PREDAJA";
    }
}