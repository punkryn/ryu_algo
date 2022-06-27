#include <iostream>
#define MAX 1501
using namespace std;


int n, table[MAX][MAX];
int cand[MAX], h[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> table[i][j];
        }
    }
    
    for(int i = 0; i < n; i++) {
        cand[i] = table[n - 1][i];
        h[i] = n - 1;
    }

    int ans = 0;
    for(int i = 0; i < n; i++) {
        int idx = 0;
        int mv = -1e10;
        for(int j = 0; j < n; j++) {
            if(mv < cand[j]) {
                idx = j;
                mv = cand[j];
            }
        }
        h[idx]--;
        cand[idx] = table[h[idx]][idx];
        ans = mv;
    }
    cout << ans << '\n';
}