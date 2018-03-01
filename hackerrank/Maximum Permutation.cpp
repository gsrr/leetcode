#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define LIM 200111

char t[LIM];
int n;
int sa[LIM];
int sai[LIM<<1];
int lcp[LIM];
ll key[LIM];

bool comp(int i, int j) {
    return key[i] < key[j];
}

void pad(bool len = false) {
    if (!len) n = strlen(t);
    t[n++] = '$';
}

void fill_sai() {
    sort(sa, sa + n, comp);
    sai[sa[0]] = 0;
    for (int i = 1; i < n; i++) {
        sai[sa[i]] = key[sa[i]] == key[sa[i - 1]] ? sai[sa[i - 1]] : i;
    }
}

void get_suffix_array() {
    for (int i = 0; i < n; i++) {
        sa[i] = i;
        sai[i] = sai[i+n] = -1;
        key[i] = t[i];
    }
    fill_sai();
    for (int p = 1; p <= n; p <<= 1) {
        for (int i = 0; i < n; i++) key[i] = sai[i]*(n+1LL) + sai[i + p];
        fill_sai();
    }
}

void get_lcp() {
    int l = 0;
    for (int i = 0; i < n; i++) lcp[i] = 0;
    for (int i = 0; i < n-1; i++) {
        int k = sai[i];
        int j = sa[k - 1];
        while (t[i + l] == t[j + l]) l++;
        lcp[k] = l;
        if (l > 0) l--;
    }
}

char w[LIM];
int freq[LIM][26];
int target[26];
void solve() {
    scanf("%s%s", w, t);
    int m = strlen(w);
    pad();
    get_suffix_array();
    get_lcp();

    for (int i = n-1; i--;) {
        for (int v = 0; v < 26; v++) {
            freq[i][v] = freq[i+1][v];
        }
        freq[i][t[i] - 'a']++;
    }

    for (int v = 0; v < 26; v++) target[v] = 0;
    for (int i = 0; i < m; i++) {
        target[w[i] - 'a']++;
    }

    int a = -1;
    int act = 0;
    int ct = 0;
    for (int i = 0; i < n; i++) {
        if (lcp[i] < m) ct = 0;
        ct++;
        int x = sa[i];
        if (x+m < n && act < ct) {
            bool ok = true;
            for (int v = 0; v < 26; v++) {
                if (freq[x][v] - freq[x+m][v] != target[v]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                a = x;
                act = ct;
            }
        }
    }

    if (a == -1) {
        puts("-1");
    } else {
        t[a + m] = 0;
        puts(t + a);
    }
}

int main() {
    int z;
    scanf("%d", &z);
    while (z--) solve();
}
