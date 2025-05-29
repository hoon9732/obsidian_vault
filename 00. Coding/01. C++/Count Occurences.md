```
#include <iostream>
using namespace std;

int main() {
    int N, V, count = 0;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        if (num == V) count++;
    }

    cin >> V;
    cout << count << '\n';

    return 0;
}

```
#Code