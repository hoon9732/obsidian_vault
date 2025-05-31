```
#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    cin >> s;

    int a[26];
    fill(a, a + 26, -1);    

    for (int i = 0; i < s.size(); ++i)
        if (a[s[i] - 'a'] == -1) a[s[i] - 'a'] = i;

    for (int i = 0; i < 26; ++i)
        cout << a[i] << ' ';
    cout << '\n';

    return 0;
}

```
#Code #String 