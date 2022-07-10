#include <bits/stdc++.h>
#define MAX 1000000
typedef long long ll;
using namespace std;

int n, height, treeSize;
vector<ll> seg;

void update(int left, int right, int idx, int a, int b) {
    if(right < a || a < left) return;
    seg[idx] += b;
    if(left == right) return;
    int mid = (left + right) / 2;
    update(left, mid, idx * 2, a, b);
    update(mid + 1, right, idx * 2 + 1, a, b);
}

int bs(int left, int right, int idx, int a) {
    if(left == right) return left;

    int mid = (left + right) / 2;
    if(seg[idx * 2] >= a) {
        return bs(left, mid, idx * 2, a);
    }
    return bs(mid + 1, right, idx * 2 + 1, a - seg[idx * 2]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n;
    height = (int)ceil(log2(MAX));
    treeSize = 1 << (height + 1);
    seg.resize(treeSize);
    for(int i = 0; i < n; i++) {
        int op;
        cin >> op;
        if(op == 2) {
            int a, b;
            cin >> a >> b;
            update(1, MAX, 1, a, b);
        } else {
            int a;
            cin >> a;
            int pos = bs(1, MAX, 1, a);
            cout << pos << '\n';
            update(1, MAX, 1, pos, -1);
        }
    }

    return 0;
}