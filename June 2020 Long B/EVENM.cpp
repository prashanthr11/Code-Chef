
# include <bits/stdc++.h>
# define endl '\n'
// # define int long long

using namespace std;

void print(vector<vector<int>> a, int n) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; ++j) {
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }
}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<vector<int>> a(n, vector<int> (n));
        int cnt = 1;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                a[i][j] = cnt;
                cnt++;
            }
        }
        if(n % 2) {
            print(a, n);    
        }
        else {
            for(int k = 1; k < n; k += 2) {
                rotate(begin(a[k]), begin(a[k]) + 1, end(a[k]));
            }
            print(a, n);
        }
        
    }
}