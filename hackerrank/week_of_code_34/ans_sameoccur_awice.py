from sys import stdin
rrm = lambda: map(int, stdin.readline().strip().split())
N, Q = rrm()
A = rrm()
from collections import defaultdict as ddic
waves = ddic(list)
for i, x in enumerate(A):
    waves[x].append(i)

def memoize(f):
    class M(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return M(f)

@memoize
def solve(x, y):
    wx = waves.get(x, [])
    wy = waves.get(y, [])
    
    count = [0] * (N+10)
    i = j = bal = ans = 0
    cur = -1
    
    while i < len(wx) and j < len(wy):
        if wx[i] <= wy[j]:
            old = count[bal]
            new = wx[i] - cur
            ans += new * (new + 2*old - 1) / 2
            count[bal] += new
            cur = wx[i]
            bal += 1
            i += 1
        else:
            old = count[bal]
            new = wy[j] - cur
            ans += new * (new + 2*old - 1) / 2
            count[bal] += new
            cur = wy[j]
            bal -= 1
            j += 1
            
    while i < len(wx):
        old = count[bal]
        new = wx[i] - cur
        ans += new * (new + 2*old - 1) / 2
        count[bal] += new
        cur = wx[i]
        bal += 1
        i += 1
        
    while j < len(wy):
        old = count[bal]
        new = wy[j] - cur
        ans += new * (new + 2*old - 1) / 2
        count[bal] += new
        cur = wy[j]
        bal -= 1
        j += 1
        
    old = count[bal]
    new = N - cur
    ans += new * (new + 2*old - 1) / 2
    return ans
    

for _ in xrange(Q):
    x, y = rrm()
    if x not in waves: x = None
    if y not in waves: y = None
    if y>x: x,y=y,x
        
    print solve(x,y)
