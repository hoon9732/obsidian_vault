```
#include <iostream>

using namespace std;

int main() {
    int N, M;
    int arr[100][100] = {0};
    
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int num;
            cin >> num;
            arr[i][j] += num;
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}
```
#Code #Array 