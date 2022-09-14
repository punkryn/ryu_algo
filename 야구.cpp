#include <bits/stdc++.h>

using namespace std;

int n, r[51][9];
int ans;
int per[10];
int used[10];

int hit(int state[4], int k, int q[9]) {
    int cnt = 0;
    for(int i = 3; i >= 0; i--) {
        if(state[i] == -1) continue;
        if (i + k > 3) {
            q[state[i]] = 1;
            state[i] = -1;
            cnt += 1;
        } else {
            state[i + k] = state[i];
            state[i] = -1;
        }
    }
    return cnt;
}

int calc() {
    int point = 0;
    int idx = 0;

    for(int i = 0; i < n; i++) {
        int flag[9], state[4];
        fill(flag, flag + 9, 1);
        fill(state, state + 4, -1);
        

        int outCount = 0;

        while(outCount < 3) {
            while(true) {
                if(flag[per[idx]]) break;

                idx = (idx + 1) % 9;
            }

            int cur = per[idx];
            flag[per[idx]] = 0;
            state[0] = cur;

            if (1 <= r[i][cur] && r[i][cur] <= 4) 
                point += hit(state, r[i][cur], flag);
            else {
                outCount += 1;
                flag[per[idx]] = 1;
            }

            idx = (idx + 1) % 9;
        }
    }

    return point;
}

void go(int depth) {
    if(depth == 9) {
        int result = calc();
        
        
        ans = max(ans, result);
        return;
    }

    if (depth == 3) {
        go(depth + 1);
        return;
    }

    for(int i = 1; i < 9; i++) {
        if (used[i]) continue;

        used[i] = 1;
        per[depth] = i;
        go(depth + 1);
        per[depth] = 0;
        used[i] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    used[0] = 1;

    cin >> n;
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < 9; j++) {
            char tmp;
            cin >> tmp;
            r[i][j] = tmp - '0';
        }
    }

    go(0);

    cout << ans;
}