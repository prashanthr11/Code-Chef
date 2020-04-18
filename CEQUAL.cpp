# include <iostream>
# include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        
        bool flag = true;
        map<int, int> mp;
        for(int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            mp[a]++;
        }
        for(auto i:mp) {
            if(i.second > 1) {
                flag = false;
                break;
            }
        }
        if(flag)
        cout << "No" << endl;
        else cout <<  "Yes" << endl;
    }
}
