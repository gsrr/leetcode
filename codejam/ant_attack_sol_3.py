def solve(w):
    d = {1: w[0]}
    for i in range(1, len(w)):
        dd = {1: set([w[i]])}
        for k, v in d.items():
            dd[k] = dd.get(k, set())
            dd[k].add(v)
            if v <= w[i] * 6:
                dd[k + 1] = dd.get(k + 1, set())
                dd[k + 1].add(v + w[i])
        d = {}
        for k, v in dd.items():
            d[k] = min(v)
    return max(d.keys())


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    w = [int(x) for x in input().strip().split(' ', n)]
    ans = solve(w)
    print('Case #{}: {}'.format(i, ans))
