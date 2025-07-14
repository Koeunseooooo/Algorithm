#include <bits/stdc++.h>

using namespace std;

vector<string> split(const string input, string delimeter){
    auto start = 0;
    auto end = input.find(delimeter);
    vector<string> result;
    while (end != string::npos)
    {
        result.push_back(input.substr(start, end - start));
        start = end + delimeter.size();
        end = input.find(delimeter, start);
    }
    result.push_back(input.substr(start));
    return result;
}
int main()
{
    string str = "apple->banana->orange->grape";
    vector<string> fruits = split(str, "->");
    for(const string fruit : fruits){
        cout << fruit << " ";
    }
    return 0;
}

/*
📌 차이점: const string vs const string&
const string input: 문자열을 값으로 복사해서 받습니다. 함수 안에서 input은 원본 문자열의 복사본이에요.
const string& input: 문자열을 참조로 전달합니다. 복사를 하지 않고, 원본을 읽기 전용으로 참조합니다.
*/

/*
🧠 의미:
const string&가 성능 면에서 더 효율적입니다, 특히 입력 문자열이 길 때 복사 비용이 줄어듭니다.
string delimeter는 복사해도 크게 부담이 없으므로 그대로 놔둬도 괜찮아요. 필요하다면 이것도 const string& delimeter로 바꿔도 좋아요.
*/
