#include <iostream>
#define MAXN 5000010
#define INF 1234567890
using namespace std;

int n, l;
int a[MAXN], tree[MAXN * 4];
int MIN(int a, int b) {
    return a < b ? a : b;
}
int MAX(int a, int b) {
    return a > b ? a : b;
}

void init(int s, int e, int v) {
    if(s == e) return tree[v] = a[s];
    
    int mid = (s + e) / 2;
    return tree[v] = MIN(init(s, mid, v * 2), init(mid + 1, e, v * 2 + 1));
}

int query(int s, int e, int v, int l, int r) {
    if (e < l || r < s)
        return INF;
    
    if (l <= s && e <= r)
        return tree[v];
    
    int mid = (s + e) / 2;
    return MIN(query(s, mid, v * 2, l, r), query(mid + 1, e, v * 2 + 1, l, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> l;
    for(int i = 0; i < n; i++)
        cin >> a[i];
    
    init(0, n - 1, 1);
    for(int i = 0; i < n; i++) {
        cout << query(0, n - 1, 1, MAX(0, i - l + 1), i) << ' ';
    }
}