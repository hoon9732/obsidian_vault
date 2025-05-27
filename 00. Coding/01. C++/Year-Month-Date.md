```
#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    time_t now = time(0);
    tm *ltm = localtime(&now);

    cout << ltm->tm_year + 1900 << '-'
         << setfill('0') << setw(2) << ltm->tm_mon + 1 << '-'
         << setfill('0') << setw(2) << ltm->tm_mday << '\n';

    return 0;
}

```
[[Efficient I-O Optimization]]
[[Formatted Output]]
[[Time and Data Retrieval]]
#Code 