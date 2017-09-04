import sys

def flip_all(arr):
        t = []
        for i in xrange(len(arr)):
                t.append(arr[i] ^ 1)
        return t

def flip_even(arr):
        t = []
        for i in xrange(len(arr)):
                if i % 2 == 0:
                        t.append(arr[i] ^ 1)
                else:
                        t.append(arr[i])
        return t

def flip_odd(arr):
        t = []
        for i in xrange(len(arr)):
                if i % 2 != 0:
                        t.append(arr[i] ^ 1)
                else:
                        t.append(arr[i])
        return t

def flip_3kp1(arr):
        t = list(arr)
        cnt = 0
        idx = 0
        while idx < len(t):
                t[idx] = t[idx] ^ 1
                cnt += 1
                idx = 3 * cnt + 1 - 1
        return t

def findall(dic, m):
        if m == 0:
                return dic

        ndic = {}
        for k in dic.keys():
                lk = eval(k)
                for f in [flip_all, flip_even, flip_odd, flip_3kp1]:
                        ndic[str(f(lk))] = True

        return findall(ndic, m - 1)


n, m = int(sys.argv[1]), int(sys.argv[2])
a = [0] * n
dic = {
        str(a) : True,
}
ndic = findall(dic, m)
print ndic
print len(ndic.keys())
