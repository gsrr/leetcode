import random

def matrix(n):
    m = [[0] * n for i in xrange(n)]
    return m

def matrix01(n):
    m = [[0] * n for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(i):
            val = random.randint(1, 10) % 2
            m[i][j] = val
            m[j][i] = val
    return m

def test_matrix():
    print matrix(3)
    print matrix01(3)

def main():
    test_matrix()
    
if __name__ == "__main__":
    main()
