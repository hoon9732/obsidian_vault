```
#include <iostream>
#incluide <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	cin >> s;
	int sum = 0, idx = -1;

	for (int i = 0; i < 13; ++i) {
		if (s[i] == '*') { idx = i; continue; }
		sum += (s[i] - '0') * ((i % 2 == 0) ? 1 : 3);
	}

	for (int d = 0; d < 10; ++d) {
		
	}


}

```
#Code #Encapsulation 