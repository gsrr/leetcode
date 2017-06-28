k=3
n = 3
MOD = 10**9 + 7
dp = [1]
for x in range(2, n + 1):
    ndp = []
    num = 0
    for y in range(min(1 + x * (x - 1) / 2, k + 1)):
        print dp
        if y < len(dp): num = (num + dp[y])
        print x, y, num
        if y >= x: num = (num - dp[y - x])
        print x, y, num
        ndp.append(num)
    dp = ndp
print dp
