#include <bits/stdc++.h>

using namespace std;

int n, m;
int j;
int tmp;
int l = 0;
int r = 10;
int dis = 0;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    cin >> j;

    // 바구니 크기 조정
    r = l + m - 1;

    for (int i = 0; i < j;i++){
        cin >> tmp; // 사과의 위치
        if(l <= tmp <=r){
            continue;
        }
        else
        {
            if(tmp<l){
                dis += l - m;
            }
            else if(tmp>r){
                dis += m - r;
            }
        }
    }

    cout << dis << '\n';
}