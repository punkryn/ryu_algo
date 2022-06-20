#include <iostream>
#include <math.h>

using namespace std;

int length, width, height, n;
int cube[20];
bool flag;

int dnq(int l, int w, int h) {
    if(l == 0 || w == 0 || h == 0) {
        return 0;
    }

    int k = l;
    if(w < k) k = w;
    if(h < k) k = h;

    int t = log2(k);
    while(t >= 0) {
        if(!cube[t]) {
            t--;
            continue;
        }

        cube[t] -= 1;
        int cnt = pow(2, t);
        return dnq(l - cnt, cnt, h) + dnq(l, w - cnt, h) + dnq(cnt, cnt, h - cnt) + 1;
    }
    flag = true;
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> length >> width >> height;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        cube[a] = b;
    }

    flag = false;
    int ans = dnq(length, width, height);
    if(flag) cout << -1;
    else cout << ans;
}