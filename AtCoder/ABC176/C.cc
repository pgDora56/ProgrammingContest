#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int total = 0;
    int prev = 0;
    for(int i = 0; i < n; i++){
        int a; cin >> a;
        cout << a << endl;
        if(prev > a) total += prev - a;
        else prev = a;
    }
    cout << total << endl;
}
