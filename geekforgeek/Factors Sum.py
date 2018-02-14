#code

def factor(n):
    if n == 0:
        return 0
    ret = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret += i
            if i != int(n / i):
                ret += (int(n / i))
        i += 1
    return ret
        
t = int(input())
for i in range(t):
    n = int(input())
    ret = factor(n)
    print (ret)
