#include <iostream>
using namespace std;


int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        int a[n], b[n];
        for(int i = 0; i < n; ++i)
        cin >> a[i];
        int j = 0;
        for(int i = 0; i < n; ++i) {
            if(a[i] == 1) {
                b[j] = i;
                ++j;
            }
        }
        bool flag = true;
        for(int i = 0; i < j - 1; ++i) {
            if(abs(b[i] - b[i + 1]) < 6)
            flag = false;
        }
        if(flag)
        cout << "YES" << endl;
        else
        cout << "NO" << endl;
    }
}
