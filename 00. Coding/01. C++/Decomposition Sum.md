```
#include <iostream>
using namespace std;

int digit_sum(int n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = max(1, N - 54); i < N; ++i) {
        if (i + digit_sum(i) == N) {
            cout << i << '\n';
            return 0;
        }
    }
    cout << '0\n';
    
    return 0;
}

```
#Code 