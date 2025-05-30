```
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int time = N * 60 + M;
    if (time < 45) time += 1440; 
    cout << (time - 45)/60 << ' ' << (time - 45) % 60 << '\n';
    
    return 0;
}

```
#Code