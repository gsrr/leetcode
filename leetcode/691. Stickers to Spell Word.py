class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        dp = [0] + [-1] * ((1 <<  len(target)) - 1)
        tcnt = collections.Counter(target)
        scnts = [collections.Counter(s) & tcnt for s in stickers]
        for x in range(len(scnts) - 1, -1, -1):
            if any(scnts[x] & scnts[y] == scnts[x] for y in range(len(scnts) - 1, -1, -1) if x != y):
                scnts.pop(x)
        
        print dp
        for status in range(1 << len(target)):
            if dp[status] < 0: continue
            for scnt in scnts:
                nstatus = status
                cnt = collections.Counter(scnt)
                for i, c in enumerate(target):
                    if cnt[c] > 0 and status & (1 << i) == 0:
                        nstatus |= (1 << i)
                        cnt[c] -= 1
                if dp[nstatus] < 0 or dp[nstatus] > dp[status] + 1:
                    dp[nstatus] = dp[status] + 1
        print dp
        return dp[-1]
