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
    return cs

jperm_cnt = 0
def jpermutations(arr, s):
    global jperm_cnt
    if s == len(arr) - 1:
        print arr
        jperm_dic[str(arr)] += 1
        jperm_cnt += 1
        return
    hist = {}
    for i in xrange(s, len(arr)):
        if hist.has_key(arr[i]) == False:
            arr[s], arr[i] = arr[i], arr[s]
            jpermutations(arr, s + 1)
            arr[s], arr[i] = arr[i], arr[s]
            hist[arr[i]] = True

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

def perms(arr, s, e):
    if s == e - 1:
        print arr
        return 
    for i in xrange(s, e):
        arr[s], arr[i] = arr[i], arr[s]
        perms(arr, s + 1, e)
        arr[i], arr[s] = arr[s], arr[i]
    
def combins(arr, k, ret):
    if k == 0:
        print ret
    for i in xrange(len(arr)):
        ret.append(arr[i]) 
        combins(arr[i + 1:], k - 1, ret)
        ret.pop()

def test_combins():
    arr = range(1,10)
    ret = []
    combins(arr, 3, ret)
    
def test_perms():
    arr = range(1,4)
    perms(arr, 0, len(arr))

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

def test_permutations():
    arr = [1,2,3,4,5,]
    dic_p = {}
    for i in xrange(len(arr)):
        dic_p[arr[i]] = i
    print dic_p
    ps = permutations(arr)
    cnt = 0
    for line in ps:
        print line
        find = True
        for i in xrange(len(line)):
            oi = dic_p[line[i]]
            if oi == i:
                find = False
                break
        if find:
            cnt += 1
    print cnt

def test_permutations_v2():
    arr = ["(", ")"] * 3
    cs = permutations(arr)
    cnt = 0 
    for line in cs:
        print "".join(line)
        cnt += 1
    print cnt

def test_jpermuations():
    global jperm_cnt
    arr = ["(", ")"] * 3
    arr = ["x", "y"] * 3
    #arr = [1,2,3]
    jpermutations(arr, 0)
    print jperm_cnt
    print jperm_dic
    print len(jperm_dic.keys())

def is_num_palindrome(n):
    sn = str(n)
    for i in xrange(len(sn)/2):
        if sn[i] != sn[len(sn) - 1 - i]:
            return False
    return True

def shuffle():
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        orig = range(1,4)
        nl = list(orig)
        for i in xrange(len(nl)):
            ni = random.randint(i, len(nl) - 1)
            nl[i], nl[ni] = nl[ni], nl[i]
        return nl

def find_all_sarr(q, arr):
    cnt = 0
    for i in xrange(0, len(arr)):
        si = collections.defaultdict(int)
        for j in xrange(i, len(arr)):
            si[arr[j]] += 1
            if si.get(q[0],0) == si.get(q[1],0):
                cnt += 1
    return cnt

def test_multi():
    n = 7
    base = pow(10, n - 1)
    #up = 1337
    up = pow(10, n)
    max_val = 0
    for i in xrange(up, base, -1):
        for j in xrange(i - 1, base, -1):
            if is_num_palindrome( i * j ):
                if i * j > max_val:
                    max_val = i * j
                else:
                    break
                im = i % 1337
                jm = j % 1337
                print i, j, i * j, (i * j) % 1337 
                print im, jm, im * jm, (im * jm) % 1337 

def test_multi_2():
    base = 1
    up = 1337
    for i in xrange(up, base, -1):
        for j in xrange(i - 1, base, -1):
            print i, j, i * j, (i * j) % 1337 

def test_find_all_sarr():
    print find_all_sarr((1,2), [1,2,1,4])

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
