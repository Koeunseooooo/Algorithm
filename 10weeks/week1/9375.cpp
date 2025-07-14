#include <bits/stdc++.h>

using namespace std;

int n;


vector<string> split(const string& input, string delimeter){
    vector<string> result;
    auto start = 0;
    auto end = input.find(delimeter);

    while(end!=string::npos){
        result.push_back(input.substr(start, end - start));
        start = end + delimeter.size();
        end = input.find(delimeter, start);
    }
    result.push_back(input.substr(start));
    return result;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n;i++){
        int k;
        cin >> k;
        map<string, int> mp;
        for (int j = 0; j < k;j++){
            string tmp;
            cin.ignore();
            getline(cin, tmp);
            vector<string> tmp_mp = split(tmp, " ");
            mp[tmp_mp[1]]++;
        }

        int res = 1;
        for (auto it : mp)
        {
            res *= it.second +1;
        }

        cout << res - 1 << '\n';
    }
}