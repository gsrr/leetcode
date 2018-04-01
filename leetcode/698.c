const int N = 16;
int dp[N][1 << N];
int sum[1 << N];

class Solution {
public:
    vector<int> a;
    int n, target;
    int solve(int mask, int k) {
        int& ret = dp[k][mask];
        if (ret >= 0) return ret;
        if (k == 1) {
            return ret = (sum[mask] == target);
        }
        ret = 0;
        for (int u = mask; u; u = (u - 1) & mask) {
            if (sum[u] == target && solve(mask ^ u, k - 1)) return ret = 1;
        }
        return ret;
    }
    bool canPartitionKSubsets(vector<int>& a, int k) {
        this->a = a;
        n = a.size();
        sum[0] = 0;
        for (int k = 1; k < (1 << n); ++k) {
            int i = 0;
            for (; i < n; ++i)
                if (k & (1 << i)) break;
            sum[k] = sum[k ^ (1 << i)] + a[i];
        }
        if (sum[(1 << n) - 1] % k) return false;
        target = sum[(1 << n) - 1] / k;
        memset(dp, 255, sizeof(dp));
        return solve((1 << n) - 1, k) == 1;
    }
};