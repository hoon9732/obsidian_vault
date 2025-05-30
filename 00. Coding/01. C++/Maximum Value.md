```
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, max = -1, cnt = 0;

    for (int i = 0; i < 9; ++i) {
        cin >> x;
        if (x > max) max = x, cnt = i + 1;
    }
    cout << max << '\n' << cnt << '\n';
    
    return 0;
}

```
#Code