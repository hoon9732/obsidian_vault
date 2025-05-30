```
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);
    
    int cnt = 0;
    bool in_word = false;
    
    for (char c : s) {
        if (c != ' ' && !in_word) {
            in_word = true;
            cnt++;
        } else if (c == ' ') {
            in_word = false;
        }
    }

    cout << cnt << '\n';
    return 0;
}

```
#Code #String