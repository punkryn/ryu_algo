#include <iostream>

using namespace std;

int n, m;
long double w[100][2];

int get_max() {
    int idx = 0;
    long double tmp = 0;
    for(int i = 0; i < n; i++) {
        if (tmp < w[i][0]) {
            tmp = w[i][0];
            idx = i;
        }
    }
    return idx;
}

int get_min() {
    int idx = 0;
    long double tmp = w[0][0];
    for(int i = 0; i < n; i++) {
        if (tmp > w[i][0]) {
            tmp = w[i][0];
            idx = i;
        }
    }
    return idx;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> w[i][0];
    }
    cin >> m;

    long double ans = w[get_max()][0] - w[get_min()][0];
    while(m--) {
        int idx = get_max();
        long double ori = w[idx][0] * (w[idx][1] + 1);
        w[idx][0] = ori / (w[idx][1] + 2);
        w[idx][1] += 1;
        long double cur = w[get_max()][0] - w[get_min()][0];
        if(ans > cur) {
            ans = cur;
        }
    }
    printf("%.10Lf", ans);
}