#include <bits/stdc++.h>

using namespace std;

int cnt[100];
string input; // 입력
string ret;   // 출력
char mid; // 유일함. 있거나 아님 아예 없거나

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> input;
    
    for (char st : input) cnt[st]++;

    int flag = 0; // 펠림드롬 가능/불가능 판단 플래그

    for (int i = 'Z'; i >= 'A';i--){
        if(cnt[i]){
            if(cnt[i]&1){ // 홀수라면
                mid = char(i);
                flag++;
                cnt[i]--;
                
            }
            if(flag>=2){
                break;
            }
            // ccc(c) bbbb aa
            for (int j = 0; j < cnt[i];j+=2){ // 한 번에 앞,뒤 두개씩 나가니까 jump도 2씩
                ret = char(i) + ret; // 앞에 하나 붙이고
                ret += char(i); // 뒤에 하나 붙이고
            }
        }
    }

    if(flag==2){
        cout << "I'm Sorry Hansoo" << '\n';
    }
    else{
        if (mid)
        {
            ret.insert(ret.begin()+ret.size()/2, mid);
        }
        cout << ret << '\n';
    }
}