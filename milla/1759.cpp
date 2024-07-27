#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 15
using namespace std;

int L,C;
char arr[MAX];
vector<char> v;
bool visited[MAX];
char vowels[] = "aeiou";
int vowelMin = 1;
// 입력되는 알파벳은 모두 소문자이다.
// strchr 뜻이 뭐지?
bool isValid(){ // 인자로 배열 전달 ?
    int vowelCount=0;
    for(int i=0;i<L;i++){
        if(strchr(vowels,v[i])){
            vowelCount++;
        }
    }
    return (vowelCount > vowelMin ? true : false);
    
}
void dfs(int level){
    if (level==L){
        if(isValid()){
            for (int i=0;i<L;i++){
                cout << v[i];
            }
            cout << "end" << endl;
        }
        
        
        return;
    }
    for(int i=level;i<C;i++){
        // if (!visited[i]){
        //     visited[i]=1;
            //ans[level]=arr[i];
            v.push_back(arr[i]);
            dfs(level+1);
            v.pop_back();
            // visited[i]=0;
            // ans[level]='';
        // }
        // if (!visited[i]){
        //     visited[i]=1;
        //     ans[level]=arr[i];
        //     dfs(level+1);
        //     visited[i]=0;
        //     // ans[level]='';
        // }
    }
    return;
}

int main(void){
    cin >> L >> C;
    for(int i=0;i<C;i++){
        cin >> arr[i];
    }
    sort(arr,arr+C);
    // for(int i=0;i<C;i++){
    //     cout << arr[i];
    // }
    dfs(0);
}

// #include <bits/stdc++.h>
// using namespace std;
// typedef long long int ll;
// int L,C;
// vector<char> v; 
// vector<char> res;

// bool check()
// {
//     int moum = 0;
//     for(int i = 0 ; i< L ; i++)
//     {
//         if(res[i] == 'a' ||
//            res[i] == 'e' ||
//            res[i] == 'i' ||
//            res[i] == 'o' ||
//            res[i] == 'u')
//            moum++;
//     }
//     // 모음의 수 1개 이상, 자음의수 = 전체수 -모음의 수 . 2개이상.
//     if(moum >=1 && L-moum >=2) return true; 
//     return false;
// }
// void dfs(int d){
//     if((int)res.size()==L){
//         if(check()){ //check에서 조건 부합시 출력.
//             for(int k = 0 ; k< L ; k++)
//             {
//                 cout << res[k];
//             }
//             cout << '\n';
//         }
//         return;
//     }
//     for(int i = d ; i< C; i++)
//     {
//         res.push_back(v[i]); //들어갈때 하나씩 추가해주고
//         dfs(i+1);
//         res.pop_back(); //나오면 하나 빼주고.
//     }
//     return;
// }
// int main(void)
// {
//     cin >> L  >> C;
//     for(int i = 0 ; i< C ; i++)
//     {
//         char temp;
//         cin >> temp;
//         v.push_back(temp);
//     }
//     sort(v.begin(), v.end()); //정렬하고 dfs(0)시작.
//     dfs(0);
// }
