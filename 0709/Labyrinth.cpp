#include <bits/stdc++.h>

using namespace std;

#define MAX 1001

int r, c;
char MAP[MAX][MAX];
int root, ans;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while(t--) {
        cin >> c >> r;
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                cin >> MAP[i][j];
            }
        }
        
    }
    return 0;
}