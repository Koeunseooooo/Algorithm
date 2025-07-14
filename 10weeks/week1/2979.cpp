#include <bits/stdc++.h>

using namespace std;

int a, b, c;
int cnt[101];
int sum;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a >> b >> c;
    for (int i = 0; i < 3;i++){
        int tmp_s, tmp_e;
        cin >> tmp_s >> tmp_e;
        for (int i = tmp_s; i < tmp_e;i++){
            cnt[i]++;
        }
    }

    // 계산
    for (int i = 0; i < 101;i++){
        if(cnt[i]){
            if(cnt[i]==1){
                sum += cnt[i] * a;
            }
            else if (cnt[i]==2){
                sum += cnt[i] * b;
            }
            else if (cnt[i]==3){
                sum += cnt[i] * c;
            }
        }
    }
    cout << sum;
}