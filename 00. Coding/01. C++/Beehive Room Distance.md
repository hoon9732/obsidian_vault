```
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, lay = 1;
    cin >> N;

    while(N > 1) {
        N -= (lay++ * 6);
    }
    cout << lay;

    return 0;
}

```
#Code