```
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, sizes[6], T, P;
    cin >> N;
    for (int i = 0; i < 6; ++i) cin >> sizes[i];
    cin >> T >> P;

    long long ts = 0;
    for (auto sz : sizes) ts += (sz + T - 1) / T;

    long long pb = N / P, ps = N % P;

    cout << ts << '\n' << pb << ' ' << ps << '\n';

    return 0;
}

```