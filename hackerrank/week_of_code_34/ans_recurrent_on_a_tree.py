#!/bin/python3


from sys import stdin
input = stdin.readline


MOD = 10**9 + 7


zero = (0, 0, 0)

one = (1, 0, 1)


def matadd(a, b):
    return ((a[0] + b[0]) % MOD,
            (a[1] + b[1]) % MOD,
            (a[2] + b[2]) % MOD)


def matsub(a, b):
    return ((a[0] - b[0]) % MOD,
            (a[1] - b[1]) % MOD,
            (a[2] - b[2]) % MOD)


def matsum(l):
    return tuple(sum(x) for x in zip(*l)) or (0, 0, 0)


def matmul(a, b):
    return ((a[0] * b[0] + a[1] * b[1]) % MOD,
            (a[0] * b[1] + a[1] * b[2]) % MOD,
            (a[1] * b[1] + a[2] * b[2]) % MOD
            )


def matexp(m, n):
    ans = one
    while n:
        if n & 1:
            ans = matmul(ans, m)
        m = matmul(m, m)
        n >>= 1
    return ans


fib = (1, 1, 0)


def main():

    N = int(input())

    neigh = [list() for _ in range(N)]

    for _ in range(N - 1):
        x, y = map(int, input().split())
        neigh[x - 1].append(y - 1)
        neigh[y - 1].append(x - 1)

    C = list(map(int, input().split()))

    root = max(range(N), key=lambda x: len(neigh[x]))

    level = [None] * N
    level[root] = 0
    Q = [root]
    while Q:
        v = Q.pop()
        for n in neigh[v]:
            if level[n] is None:
                level[n] = level[v] + 1
                Q.append(n)

    sons = tuple(tuple(v for v in neigh[n]
                       if level[n] < level[v])
                 for n in range(N))
    ordered = sorted(range(N), key=level.__getitem__)
#    del level, neigh

    M = tuple(matexp(fib, c) for c in C)

    """
    Sum of the fibonacci numbers of the pathes
    STARTING from n and going down
    """
    G = [None] * N
    for n in reversed(ordered):
        G[n] = (
            matmul(
                M[n],
                matadd(
                    matsum(G[v] for v in sons[n]),
                    one))
        )

    """
    Sum of the fibonacci numbers of the pathes
    having n as lowest common ancestor
    """
    ans = 0

    for n in reversed(ordered):
        s = matsum(G[v] for v in sons[n])
        ss = matmul(s, s)
        sq = matsum(matmul(G[v], G[v]) for v in sons[n])

        ans += (
            matmul(
                M[n],
                matadd(
                    matadd(
                        matsub(ss, sq),  # paths between branches
                        # paths starting and ending to n of length > 1
                        matadd(s, s)
                    ),
                    one  # path [n]
                )))[0]
        # we take [0][0] because the fibonacci sequence is shifted

        ans %= MOD
    return ans


print(main())
