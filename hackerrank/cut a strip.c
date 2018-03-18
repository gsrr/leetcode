#define _USE_MATH_DEFINES
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <complex>
#include <cmath>
#include <numeric>
#include <bitset>
#include <functional>

using namespace std;

#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr << name << ": " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');
	cerr.write(names, comma - names) << ": " << arg1 << " |";
	__f(comma + 1, args...);
}

typedef long long int64;
typedef pair<int, int> ii;
const int INF = 1 << 29;
const int MOD = 1e9 + 7;

const int N = 400;
int a[N][N], sum[N][N];
int U[N][N][N];
int A[N][N][2];
int dp[N][2];

int query(int x1, int y1, int x2, int y2) {
	return sum[x2 + 1][y2 + 1] - sum[x2 + 1][y1] - sum[x1][y2 + 1] + sum[x1][y1];
}

int solve(int a[N][N], int n, int m, int k) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + a[i][j];
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			U[i][j][1] = -a[i][j];
			for (int len = 2; i - len + 1 >= 0 && len <= k; ++len) {
				U[i][j][len] = max(U[i][j][len - 1], -query(i - len + 1, j, i, j));
			}
		}
	}
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = i; j < n; ++j) {
			int len = min(j - i + 1, k);
			for (int u = 0; u < m; ++u) {
				A[j][u][0] = query(i, u, j, u);
				A[j][u][1] = A[j][u][0] + U[j][u][len];
				if (j > i) A[j][u][1] = max(A[j][u][1], A[j - 1][u][1] + a[j][u]);
			}
			for (int u = 0; u < m; ++u) {
				dp[u][0] = A[j][u][0];
				dp[u][1] = A[j][u][1];
				if (u - 1 >= 0) {
					dp[u][0] = max(dp[u][0], dp[u - 1][0] + A[j][u][0]);
					dp[u][1] = max(dp[u][1], dp[u - 1][0] + A[j][u][1]);
					dp[u][1] = max(dp[u][1], dp[u - 1][1] + A[j][u][0]);
				}
				ret = max(ret, dp[u][0]);
				ret = max(ret, dp[u][1]);
			}
		}
	}
	return ret;
}

int main() {
	int n, m, k;
	scanf("%d%d%d", &n, &m, &k);
	int minv = INF, all = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			scanf("%d", &a[i][j]);
			minv = min(minv, a[i][j]);
			all += a[i][j];
		}
	}
	if (minv >= 0) {
		printf("%d\n", all - minv);
		return 0;
	}
	int ret = solve(a, n, m, k);
	for (int i = 0; i < n || i < m; ++i) {
		for (int j = i + 1; j < n || j < m; ++j) {
			swap(a[i][j], a[j][i]);
		}
	}
	swap(n, m);
	ret = max(ret, solve(a, n, m, k));
	printf("%d\n", ret);
	return 0;
}
