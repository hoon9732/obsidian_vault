```
#include <iostream>
#include <string>

using namespace std;

char board[50][50];

int repaint(int x, int y) {
    int w_start = 0;
    for (int i = x; i < x + 8; ++i) {
        for (int j = y; j < y + 8; ++j) {
            char expected = ((i + j) % 2 == 0) ? 'W' : 'B';
            if (board[i][j] != expected) w_start++;
        }
    }
    
    return min(w_start, 64 - w_start);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i)
        for (int j = 0; j< M; ++j)
            cin >> board[i][j];
    
    int result = 64;
    for (int i = 0; i <= N - 8; ++i)
        for (int j = 0; j <= M - 8; ++j)
            result = min(result, repaint(i, j));
    
    cout << result << '\n';

    return 0;
}

```
#Code #Recursive