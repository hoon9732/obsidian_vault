```
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, x;
    int count[10001] = {0};

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> x;
        ++count[x];
    }

    string output;
    for (int i = 1; i <= 10000; ++i)
        while (count[i]--)
            output += to_string(i) + '\n';

    cout << output;
    return 0;
}

```
