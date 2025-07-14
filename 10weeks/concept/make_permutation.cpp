#include<bits/stdc++.h>

using namespace std;

vector<int> v;

void printV(vector<int> &v){
    for(int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    cout << '\n';
}
void make_permutation(int n, int r, int depth){
    if(r==depth){
        printV(v);
        return ;
    }

    for(int i=depth;i<n;i++){
        swap(v[i],v[depth]);
        make_permutation(n,r,depth+1);
        swap(v[i],v[depth]);
    }
}
int main() {
    for(int i=1;i<=3;i++){
        v.push_back(i);
    }
    make_permutation(3,3,0);
    return 0;

    
}