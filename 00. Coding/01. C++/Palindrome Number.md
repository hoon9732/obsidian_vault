```
#include <iostream>

using namespace std;

bool isPalindrome(const string& s) {
    int len = s.size();
    for (int i = 0; i < len / 2; ++i)
        if (s[i] != s[len - 1 - i]) return false;
    return true;
}   

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    while (cin >> s && s != "0") {
        cout << (isPalindrome(s) ? "yes\n" : "no\n");
    }
    
    return 0;
}

```
#Code #Encapsulation