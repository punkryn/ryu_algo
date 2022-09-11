// https://www.acmicpc.net/problem/2206

#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

#define MAXN 1000

using namespace std;

int n,m,k;
char maps[MAXN+10][MAXN+10];
int visited[MAXN+10][MAXN+10][10+1];

struct _st
{
    int x;
    int y;
    int isBrk; // 벽 부순 횟수;
};

// 상하좌우
int dir[][2] = {{-1,0},{1,0},{0,-1},{0,1}};

void input(){
    //freopen("in.txt","r",stdin);
    cin>>n>>m>>k;
    for(int i=1;i<=n;i++){
        
        cin>>&maps[i][1];
        for(int j=1;j<=m;j++){
            maps[i][j] -= '0';
        }
    }

    // visited -1로 초기화
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            for(int kk=0;kk<=k;kk++){
                visited[i][j][kk] = -1;
            }
        }
    }
}
void prt(int k){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            
            cout << visited[i][j][k]<<' ';
            
        }
        cout<<'\n';
    }
    cout<<'\n';
}





void bfs(){
    queue<_st>q;
    q.push({1,1,0});
    visited[1][1][0] = 1;
    // for(int fr=0;fr<=k;fr++){
    //     visited[1][1][fr] = 1;
    // }
    while(!q.empty()){
        _st qv = q.front();q.pop();

        for(int i=0;i<4;i++){
            int nx = qv.x+dir[i][0];
            int ny = qv.y+dir[i][1];

            if(nx<1||ny<1||nx>n||ny>m) continue;

            if (maps[nx][ny] == 1 && qv.isBrk == k) continue;

            int nxtChance = maps[nx][ny] == 1 ? qv.isBrk + 1 : qv.isBrk;
            if (visited[nx][ny][nxtChance] != -1) continue;

            visited[nx][ny][nxtChance] = visited[qv.x][qv.y][qv.isBrk] + 1;
            if (nx == n && ny == m) return;

            q.push({nx, ny, nxtChance});

            // if(qv.isBrk<k){


            //     // 벽을 부술 기회가 있고 다음 지점이 벽일 때
            //     // for(int kk=qv.isBrk;kk<k;kk++){
            //     if(maps[nx][ny] == 1 && visited[nx][ny][qv.isBrk + 1] == -1){
            //         visited[nx][ny][qv.isBrk + 1] = visited[qv.x][qv.y][qv.isBrk]+1;
            //         if (nx == n && ny == m) return;
            //         q.push({nx, ny, qv.isBrk + 1});
            //     }
            //     else if(maps[nx][ny] != 1 && visited[nx][ny][qv.isBrk] == -1){
            //         visited[nx][ny][qv.isBrk] = visited[qv.x][qv.y][qv.isBrk] + 1;
            //         if (nx == n && ny == m) return;
            //         q.push({nx,ny, qv.isBrk});

            //     }

            //     // }
                

                
            // } else if(qv.isBrk==k){

            //     if(maps[nx][ny] == 1) continue;
            //     if(visited[nx][ny][qv.isBrk] != -1) continue;

            //     visited[nx][ny][qv.isBrk] = visited[qv.x][qv.y][qv.isBrk] + 1;
            //     if (nx == n && ny == m) return;
            //     q.push({nx,ny,qv.isBrk});
                

            // }
            

        }
    }

}

void output(){
    int ans = 1e9;
    for(int i=0;i<=k;i++){
        if(visited[n][m][i] == -1) continue;
        ans = visited[n][m][i] < ans?visited[n][m][i]:ans;
    }
    if(ans==1e9){
        cout<<-1;
    }else{
        cout<<ans;
    }

}

int main()
{
    /* code */
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    input();
    bfs();
    output();
    
    
    return 0;
}



// #include <iostream>
// #include <queue>

// using namespace std;

// #define MAX_RC (1000)
// #define MAX_K (10)

// struct STATUS {
//    int r, c;
//    int chance;
//    int dist;
// };

// int R, C, K;
// char map_maze[MAX_RC][MAX_RC+1];
// bool chk[MAX_K + 1][MAX_RC][MAX_RC];

// queue<STATUS> q;

// void Input_Data(void) {
//    cin >> R >> C >> K;
//    for (int r = 0; r < R;r++) {
//       cin >> map_maze[r];
//    }
// }

// int BFS(void) {
//    int dr[] = { 0,0,1,-1 };
//    int dc[] = { 1,-1, 0, 0};

//    q.push({ 0,0,K,1 });
//    chk[K][0][0] = true;

//    if (R == 1 && C == 1) return 1;
//    while (!q.empty()) {
//       STATUS data = q.front(); q.pop();
//       for (int i = 0; i < 4;i++) {
//          STATUS ndata;
//          ndata.r = data.r + dr[i];
//          ndata.c = data.c + dc[i];
//          ndata.dist = data.dist + 1;
//          if (0 > ndata.r || ndata.r >= R) continue;
//          if (0 > ndata.c || ndata.c >= C) continue;
//          if (map_maze[ndata.r][ndata.c] == '1' && data.chance == 0) continue;
//          ndata.chance = map_maze[ndata.r][ndata.c] == '1' ? (data.chance - 1) : data.chance;
//          if (chk[ndata.chance][ndata.r][ndata.c]) continue;

//          if (ndata.r == (R - 1) && ndata.c == (C - 1)) return ndata.dist;

//          q.push(ndata);
//          chk[ndata.chance][ndata.r][ndata.c] = true;
//       }
//    }
//    return -1;
// }

// int main(void) {
//    ios_base::sync_with_stdio(false);
//    cin.tie(nullptr);
//    cout.tie(nullptr);

//    Input_Data();

//    cout << BFS() << '\n';

//    return 0;
// }