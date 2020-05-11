#include<iostream>
#include<unordered_map>
#include<map>
using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, q;
        cin >> n >> q;
        unordered_map<char, int> mp;
        string s;
        cin >> s;
        
        for(int i = 0; i < n; ++i)
            mp[s[i]]++;
            
        int qu[q];
        
        for(int i = 0;i < q; ++i) cin >> qu[i];
        
        for(int i = 0; i < q; ++i) {
            int cnt = 0;
            for(auto z:mp) {
                if(z.second > qu[i])
                cnt += (z.second - qu[i]);
            }
            cout << cnt << endl;
        }
    }
}
