#include <bits/stdc++.h>

using namespace std;

int n, m;
int cnt;
int a[15001];
vector<int> b;

void combi(int start, vector<int> &res){
    if(res.size()==2){
        int sum = 0;
        for (auto _res : res)
        {
            sum += a[_res];
        }
        if(sum==m){
            cnt++;
        }
        return;
    }

    for (int i = start + 1; i < n;i++){
        res.push_back(i);
        combi(i, res);
        res.pop_back();
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin.tie(NULL);

    cin >> n;
    cin >> m;

    for (int i = 0; i < n;i++){
        cin >> a[i];
    }

    combi(-1, b);

    cout << cnt << '\n';

    // if(m>200000){
    //     cout << 0 << '\n';
    // }
    // else{
    //     for (int i = 0; i < n; i++)
    //         {
    //             for (int j = i+1; j < n; j++)
    //             {
    //                 if (a[i] + a[j] == m)
    //                 {
    //                     cnt++;
    //                 }
    //             }
    //         }
    // cout << cnt << '\n';
    // }
    
}