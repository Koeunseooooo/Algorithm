#include <bits/stdc++.h>

using namespace std;

const int MAX = 65;
int n;
int arr[MAX][MAX];
string res;

void printArr () {
    cout << " ===== printArr ====\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n;j++){
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }
}

void dfs(int y, int x , int size){
    
    if (n == 1)
    {
        // res += arr[y][x];
        cout << arr[y][x];
        return;
    }
    else{
        
        int origin = arr[y][x];
        int flag = 1;
        for (int i = y; i < y + size; i++)
        {
            for (int j = x; j < x + size;j++){
                if(!flag){
                    break;
                }
                if(arr[i][j]!=origin){
                    flag = 0;
                }
            }
        }
        if(flag){
            // res += origin;
            cout << origin;
        }
        else{
            // res = '(' + res;
            cout << '(';
            dfs(y, x, size / 2);
            dfs(y, x + size/2, size/ 2);
            dfs(y + size/2, x, size / 2);
            dfs(y + size/2, x + size/2, size / 2);
            // res = res + ')';
            cout << ')';
        }
        }
    
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n;i++){
        string t;
        cin >> t;
        for (int j = 0; j < n;j++){
            arr[i][j] = t[j] - '0'; // 문자로 받았으니 형변환을 위해 - '0'
        }
    }
    // printArr();
    // cout << '\n';

    dfs(0, 0, n );

    cout << res << '\n';
}