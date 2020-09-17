#include<iostream>
using namespace std;


int main() {
    int t;
    cin >> t; // Testcases
    while(t--) {
        int s;
        cin >> s;
        int a[3];
        for(int i =0; i < 3; i++) cin >> a[i];
        if(a[0] + a[1] + a[2] <= s) cout << "1" << endl;
        else if(a[0] + a[1] <= s || a[1] + a[2] <= s) cout <<  "2" << endl;
        else cout <<  "3" << endl;
    }
}
