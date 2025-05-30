```
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    cin >> N;

    while(N--) {
        int R;
        string S;
        cin >> R >> S;
        
        for (char &c : S) cout << string(R, c);
        cout << '\n';
    }

    return 0;
}

```
#Code #String 