#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, k;
    cin >> n >> k;

    bool flag = false;
    for(int i = 1; i <= sqrt(k); i++) {
        if(k % i == 0) {
            if(i - 1 + k / i - 1 == n) {
                cout << "YES";
                flag = true;
                break;
            }
        }
    }

    if(!flag) {
        cout << "NO";
    }
    return 0;
}