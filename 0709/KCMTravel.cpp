#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;

const int INF = 987654321;
const int MAXV = 101;
const int MAXM = 10001;
const int MAXK = 10001;
typedef pair<int, pair<int, int>> pi;
typedef pair<int, int> pii;

struct comp {
    bool operator()(const pi &a, const pi & b) const {
        return a.first > b.first;
    }
};

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<pi> graph[MAXV];
    for(int i = 0; i < k; i++) {
        int u, v, c, d;
        cin >> u >> v >> c >> d;
        graph[u].push_back(pi(v, pii(c, d)));
    }

    int d[MAXV][MAXM];
    for(int i = 0; i <= n; i++) {
        for(int j = 0; j <= m; j++) {
            d[i][j] = INF;
        }
    }

    priority_queue<pi, vector<pi>, comp> pq;
    d[1][0] = 0;
    pq.push(pi(0, pii(1, 0)));
    while(!pq.empty()) {
        int cur_cost, cur, cur_m;
        cur_cost = pq.top().first;
        cur = pq.top().second.first;
        cur_m = pq.top().second.second;

        pq.pop();

        if(cur_cost > d[cur][cur_m]) continue;

        for(auto &p: graph[cur]) {
            int nxt, nxt_m, nxt_cost;
            nxt = p.first;
            nxt_m = p.second.first;
            nxt_cost = p.second.second;

            int cost = nxt_cost + cur_cost;
            int mm = cur_m + nxt_m;
            if(mm <= m && cost < d[nxt][mm]) {
                d[nxt][mm] = cost;
                pq.push(pi(cost, pii(nxt, mm)));
            }
        }
    }

    int ans = INF;
    for(int i = 0; i <= m; i++) {
        ans = ans > d[n][i] ? d[n][i] : ans;
    }

    if(ans == INF) {
        cout << "Poor KCM\n";
    } else {
        cout << ans << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        solve();
    }
    
    return 0;
}