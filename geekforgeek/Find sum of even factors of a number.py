#code
def arr(n):
    '''
    Time Complexity : O(n * sqrt(n))
    '''
    ret = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            v1 = i
            v2 = n // i
            if v1 % 2 == 0:
                ret += v1
            if v2 % 2 == 0:
                ret += v2
            if v1 == v2:
                ret -= v2
        i += 1
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    print (arr(n))
