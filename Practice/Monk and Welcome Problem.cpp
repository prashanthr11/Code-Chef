#include<iostream>
using namespace std;
int main() {
	long long n;
	cin >> n;
	long long a[n], b[n];
	for(long long i = 0;i < n; ++i)
	cin >> a[i];
	
	for(long long i = 0;i < n; ++i)
	cin >> b[i];
 
	for(long long i = 0;i < n; ++i)
	cout << (a[i] + b[i]) << ' ';
}
