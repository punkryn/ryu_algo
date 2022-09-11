// #if 1
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

typedef long long int ll;
using namespace std;
#define MAXN 10000
#define MAXL 100

int n,l,m;
vector<pair<int,int>> v;
int maxx;
// 상하좌우
// int dx[4] = {-1,1,0,0};
// int dy[4] = {0,0,-1,1};


void input() {
    // freopen("in.txt","r",stdin);
   cin >> n >> l >> m;
    int x, y;
    for(int i=0;i<m;i++){
        cin >> x >> y;
        v.push_back(make_pair(x,y));
        
    }
    sort(v.begin(),v.end(),[](pair<int,int>&a,pair<int,int>&b)->bool{
        return a.first < b.first;
    });

}


void sol(){
    //물고기 기준
    for(int r=1;r<l/2;r++){
        int c= l/2 - r;
        //row 투포인터 시작
        int rpt = 0;
        for(int i=0;i<m;i++){
            // while(v[i+rpt].first <= v[i].first+r){
            //     rpt += 1;
            // }
            while (rpt < m && v[rpt].first - v[i].first <= r) {
                rpt += 1;
            }
            // rpt = rpt >= m ? m-1 : rpt;

            vector<pair<int, int>> cur;
            for(int j = i; j < rpt; j++) {
                cur.push_back(make_pair(v[j].first, v[j].second));
            }
            sort(cur.begin(), cur.end(), [](pair<int, int>&a, pair<int ,int>&b)->bool {
                return a.second < b.second;
            });

            int r_ = 0;
            for(int l_ = 0; l_ < rpt - i; l_++) {
                while(r_ < rpt - i && cur[r_].second - cur[l_].second <= c) {
                    r_++;
                }

                maxx = max(maxx, r_ - l_);
            }

            // col n^2 탐색
            // for(int j = i; j < rpt; j++){
                
            //     if(v[j].second <= v[i].second+c){
            //         cnt+=1;
            //     }
            // }

            // maxx = maxx<cnt?cnt:maxx;
            
        }
    }
    // if(maxx==0){
    //     maxx == l;
    // }
    cout<<maxx;
    
}

int main() {
   ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
   input();
    sol();
    
   return 0;
}
// #endif