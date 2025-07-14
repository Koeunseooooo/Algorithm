#include <bits/stdc++.h>

using namespace std;

int n, k;
int temp;
int psum[100001];
int ret = -100 * 100000;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    for (int i = 1; i <= n; i++)
    {
        cin >> temp;
        psum[i] = psum[i-1] + temp;
        
    }

    for (int i = k; i <= n; i ++)
    {
        ret = max(ret, psum[i]-psum[i-k]);
    }

    cout << ret << '\n';
}