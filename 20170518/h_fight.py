import sys

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    ts = 0
    i = 0
    h.sort()
    while i != n and ts <= t:
        ns = h[i] / hit
        if h[i] % hit == 0:
            ts += ns
        else:
            ts += (ns + 1)
        i += 1
    return i - 1

n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)
