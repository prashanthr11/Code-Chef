# include <iostream>
# include <climits>
using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--) 
    {
        int n;
        cin >> n;
        int a[n];
        for(int i = 0; i < n; ++i)
        cin >> a[i];
        
        int wc = 1, bc = 1, cnt = 1, maxi = 0, temp = INT_MAX;
        
        for(int i = 0; i < n - 1; ++i) {
            if(a[i + 1] - a[i] <= 2) wc++;
            else {
                maxi = max(maxi, wc);
                wc = 1;
            }
        }
        
        for(int i = 0; i < n - 1; ++i) {
            if(a[i + 1] - a[i] <= 2) cnt++;
            else {
                temp = min(cnt ,temp);
                if(temp == 1)
                break;
                cnt = 1;
            }
        }
        
        cout << min(temp, cnt) << ' ' << max(wc, maxi) << endl;
    }
}
