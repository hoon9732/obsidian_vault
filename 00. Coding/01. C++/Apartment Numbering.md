```
#include <iostream>
using namespace std;

int apt[15][15]

void pascal() {
	for (int i = 0; i < 15; ++i) apt[0][i] = i;
	for (int k = 0; k < 15; ++k)
		for (int n = 0; n < 15; ++n)
			apt[k][n] = apt[k][n-1] + apt[k-1][n];
}

int main() {

}
```
#Code #Array