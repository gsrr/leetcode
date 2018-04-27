#code


def get_primes(n):
    ret = [2, 3, 5]
    for i in range(7, n + 1):
        find = True
        for j in range(len(ret)):
            if i % ret[j] == 0:
                find = False
                break
        if find:
            ret.append(i)
    return ret

def ans(n, primes):
    '''
    time complexity : n * len(p)
    '''
    arr = [0] * 100
    for i in range(2, n + 1):
        tmp = i
        for p in primes:
            if p > i:
                break
            while tmp % p == 0:
                arr[p] += 1
                tmp = tmp // p
    cnt = 1
    for i in range(len(arr)):
        if arr[i] != 0:
            cnt *= (arr[i] + 1)
    return cnt

primes = get_primes(100)
t = int(input())
for i in range(t):
    n = int(input())
    print(ans(n, primes))
