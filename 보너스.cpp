// #include <bits/stdc++.h>

// using namespace std;

// int n, m;
// vector<pair<int, int>> a;
// int bonus[15];
// int indegree[15];

// vector<int> graph[15];
// int ans[15];

// int main() {
//   ios::sync_with_stdio(false);
//   cin.tie(0); cout.tie(0);

//   cin >> n >> m;
//   for(int i = 0; i < m; i++) {
//     int x, y;
//     cin >> x >> y;
//     a.push_back(make_pair(x, y));
//   }
  
//   for(int i = 0; i < n; i++) {
//     cin >> bonus[i];
//   }

//   sort(bonus, bonus + n, [](int a, int b) {
//     return a > b;
//   });
 
//   for(int i = 0; i < a.size(); i++) {
//     indegree[a[i].second] += 1;
//     graph[a[i].first].push_back(a[i].second);
//   }

//   queue<int> q;
//   int pos = 0;
//   for(int i = 1; i <= n; i++) {
//     if (!indegree[i]) {
//       q.push(i);
//       ans[i] = bonus[pos++];
//     }
//   }
  
//   while(!q.empty()) {
//     int cur = q.front();
//     q.pop();

//     for(auto nxt : graph[cur]) {
//       indegree[nxt] -= 1;

//       if(!indegree[nxt]) {
//         q.push(nxt);
//         ans[nxt] = bonus[pos++];
//       }
//     }
//   }

//   for(int i = 1; i <= n; i++) {
//     cout << ans[i] << ' ';
//   }
// }

#include <iostream>
 
using namespace std;
 
#define MAX_N (10)
 
int N;
int mat[MAX_N + 1][MAX_N + 1];
int bonus[MAX_N + 1];
 
int flag[MAX_N + 1];
int assign[MAX_N + 1];
int max_bonus_idx;
 
void Input_Data(void){
    int M;
     
    cin >> N >> M;
    for (int i = 0; i < M; i++){
        int n1, n2;
        cin >> n1 >> n2;
        mat[n1][n2] = 1;
    }
     
    // 최대값 인덱스 찾기 - 사장에게 배정하기 위함
    max_bonus_idx = 1;
    for (int i = 1; i <= N; i++){
        cin >> bonus[i];
        if (bonus[max_bonus_idx] < bonus[i]) max_bonus_idx = i;
    }
}
 
bool Check(int n, int bonus_n){
    for (int i = 1; i < n; i++){
        if (mat[n][i] && bonus_n <= assign[i]) return false;
        if (mat[i][n] && bonus_n >= assign[i]) return false;
    }
    return true;
}
 
int DFS(int n){
    if (n > N) return 1;
 
    for (int i = 1; i <= N; i++){
        if (flag[i]) continue;
        if (!Check(n, bonus[i])) continue;
 
        flag[i] = 1;
        assign[n] = bonus[i];
        if (DFS(n + 1)) return 1;
        flag[i] = 0;
    }
    return 0;
}
 
int main(void){
    ios_base::sync_with_stdio();
    cin.tie(nullptr);
    cout.tie(nullptr);
 
    Input_Data();
 
    flag[max_bonus_idx] = 1;
    assign[1] = bonus[max_bonus_idx];
    DFS(2);
 
    for (int i = 1; i <= N; i++)
        cout << assign[i] << ' ';
 
    return 0;
}