import math


def preprocess(arr):
    col = int(math.ceil(math.log(len(arr), 2))) + 1
    lookup = [[0] * col for _ in xrange(len(arr))]
    
    for i in xrange(len(arr)):
        lookup[i][0] = i

    for j in xrange(1, col):
        for i in xrange(len(arr)):
            if i + (1 << j) - 1 < len(arr):
                pre = arr[lookup[i][j - 1]]
                #ns = i +(1 << (j - 1))
                ns = (i + (1 << j) - 1) - (1 << (j - 1)) + 1
                cur = arr[lookup[ns][j - 1]]
                lookup[i][j] = lookup[i][j - 1] if pre < cur else lookup[i + (1 << (j - 1))][j - 1]
    return lookup

def find(arr, q, lookup):
    L = q[0]
    R = q[1]
    j = int(math.log(R - L + 1, 2))
    print L, j, R - (1 << j) + 1 , j
    return min(arr[lookup[L][j]], arr[lookup[R - (1 << j) + 1][j]])

def RMQ(arr, query):
    lookup = preprocess(arr)
    for q in query:
        print q, find(arr, q, lookup)
'''
Minimum of [0, 4] is 0
Minimum of [4, 7] is 3
Minimum of [7, 8] is 12
'''
def main():
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    query = [[0, 4], [4, 7], [7, 8]]
    RMQ(arr, query)

if __name__ == "__main__":
    main()
