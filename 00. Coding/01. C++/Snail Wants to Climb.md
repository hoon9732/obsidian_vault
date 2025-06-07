```
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, V;
    cin >> A >> B >> V;

    cout << (V - B + A - B - 1) / (A - B) << '\n';
    return 0;
}

```
#Code