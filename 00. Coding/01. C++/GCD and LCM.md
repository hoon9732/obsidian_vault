```
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B;
    cin >> A >> B;

    int g = gcd(A, B);
    cout << g << '\n' << A * B / g << '\n';

    return 0;
}

```
#Code #Recuris