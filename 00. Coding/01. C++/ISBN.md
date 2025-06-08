```
#include <iostream>
#include <string>
:contentReference[oaicite:9]{index=9}

int main() {
    :contentReference[oaicite:10]{index=10}
    :contentReference[oaicite:11]{index=11}

    string s;
    cin >> s;

    int idx = s.find('*');
    int sum = 0;

    for (int i = 0; i < 13; ++i) 
        if (i != idx) {
            int x = s[i] - '0';
            sum += (i % 2 == 0 ? 1 : 3) * x;
        }

    int w = (idx % 2 == 0 ? 1 : 3);
    for (int d = 0; d < 10; ++d) {
        if ((sum + w * d) % 10 == 0) {
            cout << d << "\n";
            break;
        }
    }

    return 0;
}

```
#Code #Encapsulation 