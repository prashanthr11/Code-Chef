# include <iostream>
# include <map>
# include <climits>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    while(t--) {
        int n;
        cin >> n;
        map<int, int> mp;
        int a[n];
        
        for (int i = 0; i < n; ++i)
        cin >> a[i];
        
        for (int i = 0; i < n; ++i) {
            if (a[i] == a[i + 1]) {
                mp[a[i]]++;
                i++;
            }
            else
            mp[a[i]]++;
        }
        
        int max = INT_MIN, temp = 0;
        for(auto i:mp) {
            if(i.second > max) {
                max = i.second;
                temp = i.first;
            }
        }
        
        cout << temp << endl;
    }
}
