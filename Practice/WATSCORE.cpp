# include <iostream>
# include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--) {
        int maximum = 0;
        int n;
        // n = rand();
        cin >> n;
        int a[n], b[n];
        map<int, int> mp;
        // map<int, int> smp;
        for(int i = 0;i < n; i++){
            cin >> a[i] >> b[i];
        }
        for(int i = 0; i < n; i++){
            if(mp[a[i]]){
                mp[a[i]] = mp[a[i]] > b[i] ? mp[a[i]] : b[i];
            }
            else if(b[i] == 0){
                mp[a[i]] =  mp[a[i]] > b[i] ? mp[a[i]] : b[i];
            }
            else {
            mp[a[i]] = b[i];
            }
        }
        // for(auto &i:mp) cout << i.first << ' ' << i.second << endl;
        // cout << endl << endl << endl;
        // for(auto &i:smp)
        // {
        //     // if(smp[a[i]]){
        //         cout << i.first << ' ' << i.second << endl;
        //     // }
        // }
        for(auto i:mp){
            if(i.first < 9)
            maximum += i.second;
        }
        cout << maximum << endl;
        // for(int i=0;i<n;i++){
        //     cout << a[i] << ' ' << b[i] << endl;
    // }
    }
}
