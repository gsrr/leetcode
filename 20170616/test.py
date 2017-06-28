
n = 3
m = 4

hist = {}
q = [(n, m)]
while len(q) != 0:
    ln, lm = q.pop(0)
    if ln < 1 or lm < 1:
        continue
    if hist.has_key((ln, lm)):
        continue
    hist[(ln, lm)] = True
    for i in xrange(0, n - ln + 1):
        for j in xrange(0, m - lm + 1):
            sx = i
            sy = j
            ex = i + ln - 1
            ey = j + lm - 1
            nums = (ex - sx + 1) * (ey - sy + 1)
            print sx, sy, ex, ey, nums
    if (ln - 1) * lm > ln * (lm - 1):
        q.append((ln - 1, lm))
        q.append((ln, lm - 1))
    else:
        q.append((ln, lm - 1))
        q.append((ln - 1, lm))
'''
for ln in xrange(n, 1, -1):
    for i in xrange(0, n - ln + 1):
        for lm in xrange(m, 0, -1):
            for j in xrange(0, m - lm + 1):
                sx = i
                sy = j
                ex = i + ln - 1
                ey = j + lm - 1
                nums = (ex - sx + 1) * (ey - sy + 1)
                cand.append([(sx, sy, ex, ey), nums])
'''             
            
'''
cand.sort(key=lambda x: x[1], reverse=True)
for ca in cand:
    dic = {}
    sx = ca[0][0]
    sy = ca[0][1]
    ex = ca[0][2]
    ey = ca[0][3]
    for i in xrange(sx, ex + 1):
        for j in xrange(sy, ey + 1):
            if dic.has_key(arr[i][j]) == False:
                dic[arr[i][j]] += 0
            dic[arr[i][j]] += 1

    find = True
    odd = 0
    if len(dic.keys()) % 2 != 0:
        odd = 1 
    for key in dic.keys():
        if dic[key] % 2 != 0:
            odd -= 1
        if odd < 0:
            find = False
            break
    if find == True:
        return len(dic.keys())
'''
