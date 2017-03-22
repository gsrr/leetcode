
def ans(n):
    if n == 1:
        return 1
    arr = [ x for x in xrange(1, n + 1) if x % 2 == 0]
    cnt = 2
    while len(arr) != 1:
        num = 0
        if cnt % 2 != 0:
            arr = [ arr[x] for x in xrange(len(arr)) if x % 2 != 0]
        else:
            if len(arr) % 2 == 0:
                arr = [ arr[x] for x in xrange(len(arr)) if x % 2 == 0]
            else:
                arr = [ arr[x] for x in xrange(len(arr)) if x % 2 != 0]

        print arr
        cnt += 1
    
    return arr[0]

n = 4
print ans(n)
n = 9
print ans(n)
n = 18
print ans(n)
n = 36
print ans(n)
