// https://www.acmicpc.net/problem/18246
#include <iostream>
#define MAX 1510

using namespace std;

int n, m;
int ps[MAX][MAX];
int seg[MAX * 2][MAX * 2];

int max(int a, int b) {
    return a > b ? a : b;
}

void init() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            seg[i + MAX][j + MAX] = ps[i][j];
        }
    }

    for (int i = MAX; i < MAX * 2; i++) {
        for (int j = MAX - 1; j > 0; j--) {
            seg[i][j] = max(seg[i][j << 1], seg[i][j << 1 | 1]);
        }
    }

    for (int i = MAX - 1; i > 0; i--) {
        for (int j = 1; j < MAX * 2; j++) {
            seg[i][j] = max(seg[i << 1][j], seg[i << 1 | 1][j]);
        }
    }
}

int query1D(int x, int y1, int y2) {
    int ret = 0;
    for (y1 += MAX, y2 += MAX + 1; y1 < y2; y1 >>= 1, y2 >>= 1) {
        if (y1 & 1) {
            ret = max(ret, seg[x][y1++]);
        }
        if (y2 & 1) {
            ret = max(ret, seg[x][--y2]);
        }
    }
    return ret;
}

int query(int x1, int y1, int x2, int y2) {
    int ret = 0;
    for (x1 += MAX, x2 += MAX + 1; x1 < x2; x1 >>= 1, x2 >>= 1) {
        if (x1 & 1) ret = max(ret, query1D(x1++, y1, y2));
        if (x2 & 1) ret = max(ret, query1D(--x2, y1, y2));
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;
    int y1, x1, y2, x2;
    for (int i = 0; i < n; i++) {
        cin >> y1 >> x1 >> y2 >> x2;
        ps[y1][x1] += 1;
        ps[y1][x2] -= 1;
        ps[y2][x2] += 1;
        ps[y2][x1] -= 1;
    }

    for (int i = 0; i < MAX; i++) {
        for (int j = 1; j < MAX; j++) {
            ps[i][j] += ps[i][j - 1];
        }
    }

    for (int j = 0; j < MAX; j++) {
        for (int i = 1; i < MAX; i++) {
            ps[i][j] += ps[i - 1][j];
        }
    }

    init();
    for (int i = 0; i < m; i++) {
        cin >> y1 >> x1 >> y2 >> x2;
        cout << query(y1, x1, y2 - 1, x2 - 1) << '\n';
    }

    return 0;
}