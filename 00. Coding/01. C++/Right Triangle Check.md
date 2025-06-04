```
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int x[3];

    while(true) {
        cin >> x[0] >> x[1] >> x[2];
        if(x[0] == 0 && x[1] == 0 && x[2] == 0) break;

        sort(x, x + 3);
        cout << (x[0] * x[0] + x[1] * x[1] == x[2] * x[2] ? "right" : "wrong") << '\n';
    }
    
    return 0;
}

```
#Code #Algorithm #Sort
