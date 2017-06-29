import collections
import itertools
import math
import random
import sys

def create_arr(n):
    return range(1, n + 1)

def create_rand_arr(n):
    return [random.randint(1,100) for x in xrange(n)]

def combinations(arr):
    cs = itertools.combinations(arr, len(arr))
    for line in cs:
        print line

def permutations(arr):
    ps = itertools.permutations(arr, len(arr))
    return ps
    
def factorial(n):
    return math.factorial(n)

def combination(n, r): # correct calculation of combinations, n choose k
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))

def pascals_triangle(rows):
    result = [] 
    for count in range(rows): 
        row = [] 
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
    return result

'''
# now we can print a result:
for row in pascals_triangle(10):
    print(row)
    print sum(row)
'''

def isort(arr, i):
    val = arr[i]
    j = i
    cnt = 0
    while j > 0 and arr[j - 1] > val:
        arr[j] = arr[j - 1]
        cnt += 1
        j -= 1
    arr[j] = val
    return cnt

def qsort(arr, s , e):
    if s >= e:
        return 
    pv = arr[e]
    j = s - 1
    for i in xrange(s, e):
        if arr[i] < pv:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j + 1], arr[e] = arr[e], arr[j + 1]
    print arr
    qsort(arr, s, j)
    qsort(arr, j + 2, e)

def alpha_set(s):
    num = 0
    for w in set(s):
        num += (1 << (ord(w) - ord('a')))
    return num

def test_isort():
    arr = create_rand_arr(10)
    cnt = 0
    for i in xrange(len(arr)):
        cnt += isort(arr, i)
        print arr
    print cnt
    return cnt

def test_qsort():
    arr = create_rand_arr(10)
    qsort(arr, 0, len(arr) - 1)

def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()

if __name__ == "__main__":
    main()
'''
dic = collections.Counter()
ps = permutations([1,2,3])
for line in ps:
    cnt = insertion_sort(list(line))
    dic[cnt] += 1
od = collections.OrderedDict(sorted(dic.items()))
print od
'''
#arr = create_arr(4)
#print combinations()
