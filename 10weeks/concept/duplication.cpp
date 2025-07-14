#include <bits/stdc++.h>

using namespace std;

vector<int> a = {1, 1, 2, 5, 1, 2, 3, 4, 5};
map<int, int> mp;
int main()
{
    // 1. map 사용
    for (int i:a)
    {
        if(mp[i])
            continue;
        else{
            mp[i] = 1;
        }
    }
    vector<int> ret;
    for(auto it:mp){
        ret.push_back(it.first);
    }
    for(int  i : ret)
        cout << i << " ";
    cout << "\n";

    // 2. unique 사용
    sort(a.begin(), a.end());
    a.erase(unique(a.begin(), a.end()), a.end());
    for (int i:a)
        cout << i << " ";
    cout << '\n';
    return 0;
}