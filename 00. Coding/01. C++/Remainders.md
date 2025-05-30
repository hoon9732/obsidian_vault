```
#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a[42] = {0};
    int cnt = 0;

    for (int i = 0; i < 10; ++i) {
        int n;
        cin >> n;
        a[n % 42]++;
    }
    
    for (int i = 0; i < 42; ++i) {
        if (a[i] > 0) cnt++;
    }   
    cout << cnt << '\n';
    
    return 0;
}

```
#Code #Array 