
# include <bits/stdc++.h>
# define endl '\n'
# define int long long

using namespace std;


int j = 1;

int solve(int t) {
    if(t % 2 == 1)
        return t/2;
    else
        solve(t/2);
}



signed main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;
    while(n--) {
        int t = 1;
        cin >> t;
        cout << solve(t) << endl;
    }
}