#include <bits/stdc++.h>

#define int long long

using namespace std;

int solve(vector<int> &a) {
    auto cnt = 0, ret = 0;
    auto n = a.size();
    
    unordered_map<int, int> mp;
    
    for(auto i = n - 1; i != 0; --i) {
        if(a[i] & 1) {
            ++cnt;
            mp[i] = cnt;
        }
    }
            
    
    for(auto i = 0; i < n; ++i) {
        if(!(a[i] & 1)) {
            auto j = i + 1;
            bool flag = true;
            while (j < n && flag == true) {
                if(mp[j]) {
                    ret += mp[j];
                    flag = false;
                }
                j++;
            }
        }
    }
    return ret;
}

signed main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        
        for(auto i = 0; i < n; ++i)
            cin >> a[i];
            
        cout << solve(a) << endl;
    }
}
