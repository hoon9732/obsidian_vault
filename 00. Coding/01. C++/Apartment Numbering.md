```
#include <iostream>
using namespace std;

int apt[15][15];

void pascal() {
	for (int i = 0; i < 15; ++i) apt[0][i] = i;
	for (int k = 1; k < 15; ++k)
		for (int n = 1; n < 15; ++n)
			apt[k][n] = apt[k][n-1] + apt[k-1][n];
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	pascal();

	int T;
	cin >> T;

	while(T--) {
		int k, n;
		cin >> k >> n;
		cout << apt[k][n] << '\n';
	}
	return 0;
}
```
#Code #Array