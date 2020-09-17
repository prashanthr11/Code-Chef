 #include <iostream>
 
using namespace std;
 
int main()
{
    int n, k;
    cin >> n >> k;
    int a[n];
    for(int i = 0; i < n; ++i)
    cin >> a[i];
    
    bool flag = false;
    
    for(int i = 0; i < n; ++i) {
        int t = k - a[i];
        for(int j = i + 1; j< n; ++j) {
            if(a[j] == t){
                flag = true;
                break;
            }
            else
            flag = false;
        }
    }
    
    if(flag)
    cout << "YES" << endl;
    else
    cout << "NO" << endl;
}
