// #include <bits/stdc++.h>

// using namespace std;

// #define MAXN 15

// int n, m;
// int matrix[MAXN][MAXN];
// int bonus[MAXN];
// int ans[MAXN];
// int used[MAXN];

// bool check(int x, int bonusN) {
//   for(int i = 1; i < x; i++) {
//     if (matrix[x][i] && bonusN <= ans[i]) return false;
//     if (matrix[i][x] && bonusN >= ans[i]) return false;
//   }
//   return true;
// }

// int dfs(int x) {
//   if (x > n) return 1;
  
//   for(int i = 1; i <= n; i++) {
//     if (used[i]) continue;
//     if (!check(x, bonus[i])) continue;

//     used[i] = 1;
//     ans[x] = bonus[i];
//     if(dfs(x + 1)) return 1;

//     used[i] = 0;
//   }
//   return 0;
// }

// int main() {
//   ios::sync_with_stdio(false);
//   cin.tie(0); cout.tie(0);

//   cin >> n >> m;
//   for(int i = 0; i < m; i++) {
//     int x, y;
//     cin >> x >> y;
//     matrix[x][y] = 1;
//   }

//   int maxPos = 1;
//   for(int i = 1; i <= n; i++) {
//     cin >> bonus[i];

//     if (bonus[maxPos] < bonus[i]) {
//       maxPos = i;
//     }
//   }
  
//   ans[1] = bonus[maxPos];
//   used[maxPos] = 1;
  
//   dfs(2);

//   for(int i = 1; i <= n; i++)
//     cout << ans[i] << ' ';
//   return 0;
// }

// 중소기업인 K 회사에서 직원들에게 보너스를 지급하려고 한다.
// 그런데 직원들의 자존심이 강해서 상급자들이 직급이 낮은 사람보다는 한 푼이라도 더 받기를 원한다.
// 단, 자기랑 직접적 관련이 없는 사람의 보너스 금액에는 관심 없다.
// 중소기업 특성상 정확한 직급이 존재하지 않고 누가 누구 상급자고 하급자인지만 정해져 있는 상황에서 사장은 골치가 아프다.
// 예를 들어 아래와 같은 조직인 경우에는 아래와 같다.
// 편의상 이름은 숫자로 대체한다.
// 1은 언제나 사장이다.
//  5명이 있고 보너스 금액은 51, 30, 35, 30, 31 일 경우 1번부터 51, 35, 31, 30, 30으로 배정하면 된다.
// 중소기업 사장을 도와서 모두가 만족할 수 있는 보너스 금액을 배정하자.

// 입력 설명
// 첫 줄에 N과 M이 입력된다. N은 직원 수 (3≤N≤10), M은 상하관계의 개수(2≤M≤100) 이다.
// 다음 줄부터 M줄에 걸쳐 상하관계가 입력된다. 각 줄에는 상급자 하급자 순으로 입력되며 공백으로 구분된다. (상하관계 오류가 발생하는 입력은 없음)
// 마지막 줄에는 보너스 금액이 N개만큼 공백으로 구분되어 입력된다. 보너스 금액은 1이상 1,000,000 이하 이다.
// 출력 설명
// 1번부터 N번까지 순서대로 공백으로 구분하여 보너스 금액을 출력한다. (답이 여러 개일 경우 그 중 한가지만 출력하면 됨)


#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define MAXN 10

using namespace std;
// typedef unsigned long long ull;
// typedef long long ll;

int n,m;
vector<int> graph[MAXN+2];
vector<int> reverse_graph[MAXN+2];
int used[MAXN+2];
int salary[MAXN+2];
int selected[MAXN+2];
void input() {
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;
        graph[x].push_back(y);
        reverse_graph[y].push_back(x);
    }

    for(int i=1;i<=n;i++){
        cin>>salary[i];
    }

    sort(salary+1,salary+n+1,[](int a,int b){
        return a>b;
    });
    used[1] = 1;
    selected[1] = salary[1];



}

int isok(int st,int bn){
    // 상급자 확인
    for(int rev:reverse_graph[st]){
        if(selected[rev] && bn>=selected[rev]) {
            return 0;
        }
    }
    // 하급자 확인
    for(int rig:graph[st]){
        if(selected[rig] && bn<=selected[rig]){
            return 0;
        }
    }
    return 1;

}
int dfs(int st) {
    // for(int i=1;i<=n;i++){
    //     cout<<selected[i]<<' ';
    // }
    // cout<<'\n';

    if(st>n) return 1;

    for(int i=1;i<=n;i++){


        if(used[i] != 0) continue;
        if(!isok(st,salary[i])) continue;
        
        used[i] = 1;
        selected[st] = salary[i];
        if(dfs(st+1)) return 1;
        
        used[i] = 0;
        
    }
    

    return 0;
    


}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    input();
    dfs(2);
    for(int i=1;i<=n;i++){
        cout<<selected[i]<<' ';
    }
    // cout<<"done";
    
}