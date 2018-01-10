


ts = "aa" * 2
fs = "baa"

print ts
print fs

def failure_function(fs):
    dp = [-1] * len(fs)
    for i in xrange(1, len(dp)):
        j = dp[i - 1]
        while fs[i] != fs[j + 1] and j > -1:
            j = dp[j]

        if fs[i] == fs[j + 1]:
            dp[i] = j + 1
    return dp

def find(ts, fs, ff):
    i = 0
    j = 0
    while i < len(ts):
        if j == len(fs):
            print i - len(fs), i - 1
            j = 0
            i = i - ff[ j - 1 ] - 1
        print fs[j], ts[i]
        if fs[j] == ts[i]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = ff[j - 1] + 1
    if j == len(fs):
        print i - len(fs), i - 1
       
ff = failure_function(fs)
print ff
print find(ts, fs, ff)

