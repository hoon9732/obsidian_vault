```
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, C, num, cnt[10] = {0};
    cin >> A >> B >> C;
    num = A * B * C;

    while (num > 0) {
        cnt[num % 10]++;
        num /= 10;
    }

    for (int i = 0; i < 10; ++i) {
        cout << cnt[i] << '\n';
    }

    return 0;
}

```
#Code #Array 