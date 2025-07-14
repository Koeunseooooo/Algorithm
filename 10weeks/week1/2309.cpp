#include <bits/stdc++.h>

using namespace std;

int k = 9;
bool isFin = 0;
void combi(int start, vector<int> org, vector<int> res)
{
    if(isFin){
        return;
    }

    if(res.size()==7){
        int sum = 0;
        vector<int> ans;
        for (int i : res)
        {
            sum += org[i];
            ans.push_back(org[i]);
        }
        if (sum == 100)
        {
            sort(ans.begin(), ans.end());
            for(int i:ans){
                cout << i << '\n';
            }
            isFin = 1;
            // cout << "success" << '\n';
            
        }
        return;
    }

    for (int i = start + 1; i < k;i++){
        res.push_back(i);
        combi(i, org, res);
        res.pop_back();
    }
}
int main() {
    vector<int> a(k);
    for (int i = 0; i <k; i++)
    {
        cin >> a[i];
    }

    vector<int> b;
    combi(-1, a, b);
}