#include <bits/stdc++.h>

using namespace std;

int n,k;
map<string,int> a_map;
map<int,string> b_map;
string tmp;
string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    for (int i=0;i<n;i++){
        cin >> tmp;
        a_map[tmp] = i+1;
        b_map[i+1] = tmp;
    }

    for (int i=0;i<k;i++){
        cin >> s;
        if(atoi(s.c_str())==0){
            cout << a_map[s] << '\n';
        }
        else{
            cout << b_map[atoi(s.c_str())] << '\n';
        }
    }
}