#include <bits/stdc++.h>
#define int long long
// # define l 1e5
# define endl '\n'
using namespace std;


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        int a[10000000];
        a[0] = 0;
        a[1] = 1;
        for(auto i = 2; i < 60; ++i)
        a[i] = (a[i - 1] + a[i - 2]) % 10;
        
        int i = 1;
        while(i <= n/2) {
            i = i * 2;
        }
        i = i % 60;
        cout << a[i - 1] << endl;
    }
}
        
