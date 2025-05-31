```
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, sum = 0;
    char c;
    cin >> N;

    while(N--) {
        cin >> c;
        sum += c - '0';
    }

    cout << sum << '\n';

    return 0;
}

```
#Code #Char