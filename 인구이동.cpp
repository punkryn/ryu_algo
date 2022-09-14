// https://www.acmicpc.net/problem/16234

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define MAXN 50
using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int n,l,r;
int A[MAXN+1][MAXN+1];
int visited[MAXN+1][MAXN+1];

struct mov
{
    /* data */
    int x;
    int y;
};

// mov path[MAXN+1];

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

void input() {
    // freopen("in.txt","r",stdin);
    cin>>n>>l>>r;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>A[i][j];
        }
    }
}


int sol(int xx, int yy) {

    queue<mov>q;
    q.push({xx,yy});

    int sum = A[xx][yy];
    int cnt = 1;

    visited[xx][yy] = 1;
    
    vector<pair<int, int>> cand;
    cand.push_back(make_pair(xx, yy));

    while(!q.empty()){
        mov qv = q.front();q.pop();

        for(int i=0;i<4;i++){
            int nx = qv.x+dx[i];
            int ny = qv.y+dy[i];

            
            
            if(nx<0||ny<0||nx>=n||ny>=n) continue;
            if(visited[nx][ny] != -1) continue;

            int isOpen = abs(A[qv.x][qv.y]-A[nx][ny]);

            if(isOpen < l || isOpen > r ) continue;

            visited[nx][ny] = 1;
            sum += A[nx][ny];
            cnt += 1;
            q.push({nx,ny});

            cand.push_back(make_pair(nx, ny));

        }


    }

    int calc = sum / cnt;
    for(auto c: cand) {
        A[c.first][c.second] = calc;
        visited[c.first][c.second] = 2;
    }
    
    return cnt != 1;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    input();

    int ans=0;
    int ansCnt = 0;
    while(1){
        ansCnt++;
        memset(visited,-1,sizeof(visited));
        bool flag = false;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(visited[i][j] != -1) continue;
                flag |= sol(i,j);
                
            }   
        }
        
        if(!flag){
            cout<<ans;
            break;
        } else{
            ans += 1;
        }
    }
    
    
    
}