```
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    while (N--) {
        string s;
        cin >> s;

        int score = 0, cnt = 1;
        for (char c : s) {
            if (c == 'O') score += cnt, cnt++;
            else cnt = 1;
        }
        cout << score << '\n';
    }

    return 0;
}

```
#Code #String 