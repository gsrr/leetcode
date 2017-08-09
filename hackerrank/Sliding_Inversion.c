#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <set>
#include <stdint.h>
#include <string.h>
using namespace std;

template <typename int_type_t>
struct fenwick_t {
	vector<int_type_t> arr;
	uint32_t sz;

	fenwick_t(uint32_t size) : arr(size, 0), sz(size) {
	}

	void clear() {
		memset(&arr[0], 0, sizeof(int_type_t)*sz);
	}

	static int_type_t lsb(int_type_t n) {
		return n&(-n);
	}

	void add(uint32_t id, int_type_t a) {
		while (id<sz) {
			arr[id]+=a;
			id+=lsb(id+1);
		}
	}

	// returns sum of a[0..id)
	int_type_t sum(uint32_t id) {
		int_type_t s=0;
		while (id) {
			s+=arr[id-1];
			id-=lsb(id);
		}
		return s;
	}

	// returns sum of a[f..t)
	int_type_t range(uint32_t f, uint32_t t) {
		int_type_t s=0;

		while (t>f) {
			s+=arr[t-1];
			t-=lsb(t);
		}

		while (f>t) {
			s-=arr[f-1];
			f-=lsb(f);
		}
		return s;
	}

	int_type_t get(uint32_t id) {
		return range(id, id+1);
	}

	void set(uint32_t id, int_type_t a) {
		add(id, a-get(id));
	}
};

int main() {
	unordered_map<int32_t, uint32_t> mp(141107);
	uint32_t n, m, i, c;
	uint64_t ans, ccnt;
	int32_t l, ii;
	ios_base::sync_with_stdio(false);
	uint64_t res;
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	fenwick_t<int32_t> f(n+2);
	vector<int32_t> a(n), b(n);
	vector<uint32_t> r(n);
	for (i=0; i<n; i++) {
		cin >> a[i];
		b[i]=a[i];
	}
	if (m==1) {
		cout << 0 << endl;
		return 0;
	}
	sort(a.begin(), a.end());
	l=a[0];
	c=0;
	mp[l]=c;
	for (i=1; i<n; i++)
		if (a[i]!=l) {
			l=a[i];
			mp[l]=++c;
		}
	for (i=0; i<n; i++)
		r[i]=mp[b[i]];
	ccnt=0;
	for (ii = m-1; ii >= 0; ii--) {
		ccnt+=f.sum(r[ii]);
		f.add(r[ii], 1);
	}
	ans=ccnt;
	for (i = m; i < n; i++) {
		ccnt -= f.sum(r[i-m]);
		f.add(r[i - m], -1);
		ccnt += f.range(r[i]+1, f.sz);
		f.add(r[i], 1);
		ans += ccnt;
	}
	cout << ans << endl;
	return 0;
}
