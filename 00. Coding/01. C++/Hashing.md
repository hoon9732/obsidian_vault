```
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L;
    string s;
    cin >> L >> s;

    const int r = 31;
    const int M = 1234567891;

    long long hash = 0, pow_r = 1;

    for (int i = 0; i < L; ++i) {
        int val = s[i] - 'a' + 1;
        hash = (hash + val * pow_r) % M;
        pow_r = (pow_r * r) % M;
    }

    cout << hash << '\n';
    return 0;
}

```
#Code