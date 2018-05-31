#include <bits/stdc++.h>

using namespace std;

const int MX = 200002, LOG = 20;

int fwt[MX];

void fwt_add(int x, int d) {
	while (x < MX) {
		fwt[x] += d;
		x += x & -x;
	}
}

int fwt_get(int x) {
	int r = 0;
	while (x) {
		r += fwt[x];
		x -= x & -x;
	}
	return r;
}

vector<int> G[MX];
int dep[MX], par[LOG][MX], f[MX], g[MX];

void dfs(int v, int p = 0, int d = 0) {
	static int t = 0;

	f[v] = ++t;

	dep[v] = d;
	par[0][v] = p;
	for (int i = 0; i + 1 < LOG; i++) par[i + 1][v] = par[i][par[i][v]];

	for (int u : G[v]) {
		if (u == p) continue;
		dfs(u, v, d + 1);
	}

	g[v] = t;
}

int lca(int u, int v) {
	if (dep[u] > dep[v]) swap(u, v);
	for (int i = LOG - 1; i >= 0; i--)
		if (dep[v] - (1 << i) >= dep[u])
			v = par[i][v];

	for (int i = LOG - 1; i >= 0; i--)
		if (par[i][u] != par[i][v]) {
			u = par[i][u];
			v = par[i][v];
		}

	return u == v ? v : par[0][v];
}

int main()
{
	int n;
	ignore = scanf("%d", &n);
	map<pair<int, int>, int> E;
	for (int i = 1, u, v; i < n; i++) {
		ignore = scanf("%d %d", &u, &v);
		u--; v--;
		G[u].push_back(v);
		G[v].push_back(u);
		E[make_pair(min(u, v), max(u, v))] = 0;
	}

	dfs(0);

	int q;
	ignore = scanf("%d", &q);
	while (q--) {
		char c;
		int u, v;
		ignore = scanf(" %c %d %d", &c, &u, &v);
		u--; v--;

		if (dep[u] > dep[v]) swap(u, v);

		if (c == 'd' || c == 'c') {
			if (E.count(make_pair(min(u, v), max(u, v))) == 0) continue;

			int d = c == 'd' ? 1 : -1;
			if (E[make_pair(min(u, v), max(u, v))] + d < 0 || E[make_pair(min(u, v), max(u, v))] + d > 1) continue;
			E[make_pair(min(u, v), max(u, v))] += d;
			fwt_add(f[v], d);
			fwt_add(g[v] + 1, -1 * d);
		}
		else {
			int w = lca(u, v);

			int cnt = fwt_get(f[u]) + fwt_get(f[v]) - 2 * fwt_get(f[w]);
			if (cnt == 0) printf("%d\n", dep[u] + dep[v] - 2 * dep[w]);
			else printf("Impossible\n");
		}
	}

	return 0;
}
