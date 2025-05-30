```
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a[8];
    string s = "mixed";

    for (int i = 0; i < 8; ++i) cin >> a[i];
    
    if (a[0] == 1) {
        s = "ascending";
        for (int i = 0; i < 8; ++i) {
            if (a[i] != i+1) s = "mixed";
        }
    }
    else if (a[0] == 8) {
        s = "descending";
        for (int i = 0; i < 8; ++i) {
            if (a[i] != 8 - i) s = "mixed";
        }
    }
    
    cout << s << '\n';
    return 0;
}

```
#Code #Array 