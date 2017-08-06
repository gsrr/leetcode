def ans(n):
    arr = map(str, xrange(1, n + 1))
    arr.sort()
    return [int(i) for i in arr]

print ans(15)
