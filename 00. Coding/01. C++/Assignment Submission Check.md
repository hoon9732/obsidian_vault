```
#include <iostream>

using namespace std;

int main() {
    bool submitted[30] = {false};
    
    for (int i = 0; i < 28; i++) {
        int num;
        cin >> num;
        submitted[num] = true;
    }
    
    for (int i = 0 ; i < 30; i++) {
        if (!submitted[i]) cout << i << '\n';
    }
    
    return 0;
}

```
#Code #Array 