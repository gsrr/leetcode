
def convert(t):
    m,s = t.split(":", 1)
    return int(m) * 60 + int(s)

def cal(a, b):
    n1 = convert(a)
    n2 = convert(b)
    return n2 - n1

def ans(ts):
    app = []
    for t in ts:
        m,s = t.split(":", 1)
        m = str(int(m) + 24)
        app.append("%s:%s"%(m,s))
    ts = ts + app
    ts.sort()
    print ts
    min_val = 0x7fffffff
    cnt = 0
    while cnt < len(ts) - 1:
        tmp = cal(ts[cnt], ts[cnt + 1])
        if tmp < min_val:
            min_val = tmp
        cnt += 1
    return min_val

s = ["23:59","00:00"]
print ans(s)
