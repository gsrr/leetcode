#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

#define ASST(x, l, r) assert(x <= r && x >= l)

const int mn = -10000000;
const int mx = 10000000;

int n, m, tot, A[10], B[10], S[30], mnA[30], mxA[30], mnB[30], mxB[30];

void gen(int* MX, int* MN, int* A, int n) {
    for(int i=1; i<=tot; i++) 
        MX[i] = mn, MN[i] = mx; // default value for max array and min array

	    cout << 0 << ":" << 0 << ":" << MX[0] << "\n";
    for(int i=1; i<=n; i++) {
        for(int j=tot; j>=A[i]; j--) {
            MX[j] = max(MX[j], MX[j-A[i]]+1);  // max number in sum = j , MX[j] = 4, means sum(4 number) == j
            MN[j] = min(MN[j], MN[j-A[i]]+1); // min number in sum = j , MN[j] = 3 , means sum(3 number) = j
            S[j] |= S[j-A[i]];
	    cout << i << ":" << j << ":" << MX[j] << "\n";
	    cout << i << ":" << j << ":" << MN[j] << "\n";
        }
    }
}

int main() {
    
    cin >> n >> m; ASST(n, 1, 100); ASST(m, 1, 100);
    for(int i=1; i<=n; i++) cin >> A[i], tot += A[i], ASST(A[i], 1, 100); 
    for(int i=1; i<=m; i++) cin >> B[i], tot += B[i], ASST(B[i], 1, 100);
   
    S[0] = 1; // 0 --> sum(A) + sum(B) = 0 , 1 --> exist
    mxA[0] = 0;
	    mnA[0] = 0;
    gen(mxA, mnA, A, n);
    gen(mxB, mnB, B, m);
    
    cout << "total:" << tot << "\n";
    int ans1, ans2, val = tot;
    for(int i=0; i<=tot; i++) {
        if(S[i] && tot - i >= i && tot - 2 * i <= val) {
            val = tot - 2 * i;
            ans1 = i;
        }
    }
    cout << "ans1:" << ans1 << "\n"; // ans1 is the sum with min_difference between A and B.

    ans2 = n + m;
    for(int i=1; i<=ans1; i++){
        if(mxA[i] <= n && mxA[i] >= 0 && mnB[ans1 - i] <= m && mnB[ans1 - i] >= 0 )
            ans2 = min(ans2, n - mxA[i] + mnB[ans1 - i]);
        if(mxB[i] <= m && mxB[i] >= 0 && mnA[ans1 - i] <= n && mnA[ans1 - i] >= 0)
            ans2 = min(ans2, m - mxB[i] + mnA[ans1 - i]);
	cout << "ans2:" << ans2 << "\n";
    }
    ans1 = tot - 2 * ans1;
    cout << ans1 << " " << ans2 << "\n";
    return 0;
}
