```
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    double score, max = 0, sum = 0;

    for (int i = 0; i < N; ++i) {
        cin >> score;
        sum += score;
        if (score > max) max = score;   
    }

    cout << fixed;
    cout.precision(2);
    cout << (sum / max * 100) / N << '\n';
    return 0;
}

```
#Code #Precision
