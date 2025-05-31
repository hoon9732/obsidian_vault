```
#include <iostream>
#include <climits>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, min = INT_MAX, max = INT_MIN;
    cin >> N;

    while(N--) {
        int M;
        cin >> M;
        if (M < min) min = M;
        if (M > max) max = M;
    }

    cout << min << ' ' << max << '\n';
    return 0;
}

```
#Code #Climits