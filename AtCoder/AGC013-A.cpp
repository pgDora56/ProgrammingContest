// ふくしま C++
// AC
#include <bits/stdc++.h>
using namespace std;
int main(){
    long n;
    cin >> n;
    if(n < 3){
        cout << 1;
        exit(0);
    }

    long a1, a2, inc, prev, cnt;
    cin >> a1 >> a2;
    inc = a2 - a1;
    prev = a2;
    cnt = 1;
    for(long i = 0; i < n-2; i++){
        long val, ninc;
        cin >> val;
        ninc = val - prev;
        if(inc * ninc < 0){
            cnt++;
            inc = 0;
        }
        else if(inc == 0){
            inc = ninc;
        }
        prev = val;
    }
    cout << cnt;
}
