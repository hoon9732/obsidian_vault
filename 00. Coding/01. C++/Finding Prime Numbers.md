```
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, x, cnt = 0;
    cin >> N;

    while(N--) {
        cin >> x;
        if (x < 2) continue;

        bool prime = true;
        for (int i = 2; i * i <= x; ++i) {
            if (x % i == 0) {
                prime = false;
                break;
            }
        }
        cnt += prime;
    }
    cout << cnt << '\n';

    return 0;
}

```
#Code #Algorithm 