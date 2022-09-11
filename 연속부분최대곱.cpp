#include <iostream>
#include <cmath>

using namespace std;

int n;
double s[10010];

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  cin >> n;
  for(int i = 0; i < n; i++) {
    cin >> s[i];
  }

  double ans = s[0];
  for(int i = 1; i < n; i++) {
    double nxt = s[i - 1] * s[i];
    if (nxt > s[i]) s[i] = nxt;
    ans = max(ans, s[i]);
  }

  printf("%.3f", ans);
  return 0;
}