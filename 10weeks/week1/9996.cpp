#include <bits/stdc++.h>

using namespace std;


int n;
string ptr;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    cin >> ptr;

    int pos = ptr.find('*');
   
    string prefix = ptr.substr(0, pos);
    string suffix = ptr.substr(pos + 1);

    for (int i = 0; i < n;i++){
        string tmp;
        cin >> tmp;
        if(prefix.size()+suffix.size()>tmp.size()){
            cout << "NE\n";
        }
        else{
            if(tmp.substr(0,prefix.size())==prefix && tmp.substr(tmp.size()-suffix.size())==suffix){
                cout << "DA\n";
            }
            else{
                cout << "NE\n";
            }
        }
        
     }
}