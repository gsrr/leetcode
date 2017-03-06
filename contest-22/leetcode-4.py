def findRotateSteps(ring, key):
    def get(i):
        return ring[i % len(ring)]

    memo = {}

    def dp(pos, k):
        if k == len(key):
            return 0
        lo = hi = pos
        himove = lomove = 0
        while get(hi) != key[k]:
            hi += 1
            himove += 1
        while get(lo) != key[k]:
            lo -= 1
            lomove += 1
        lo %= len(ring)
        hi %= len(ring)
        ans = min(dp(lo, k+1) + lomove, dp(hi, k+1) + himove) 
        memo[pos, k] = ans
        return ans

    return dp(0, 0) + len(key)

ring = "godding"
key = "gd"
print findRotateSteps(ring, key)

