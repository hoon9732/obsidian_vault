```
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    int a = 1, b = 1, c = 1;
    for (int i = 2; i <= N; ++i) a *= i;
    for (int i = 2; i <= K; ++i) b *= i;
    for (int i = 2; i <= N - K; ++i) c *= i;

    cout << a / (b * c) << '\n';
    return 0;
}

```
#Code