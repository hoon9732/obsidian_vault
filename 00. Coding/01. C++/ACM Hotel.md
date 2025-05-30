```
#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--) {
        int H, W, N;
        cin >> H >> W >> N;
        cout << ((N - 1) % H + 1) * 100 + ((N - 1) / H) + 1 << '\n';
    }

    return 0;
}

```
#Code #Math 