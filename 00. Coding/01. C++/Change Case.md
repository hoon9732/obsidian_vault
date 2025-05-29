```
#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    for (char &c : s) {
        if(islower(c)) c = toupper(c);
        else c = tolower(c);
    }

    cout << s << '\n';
    return 0;
}

```
#Code #String #Char