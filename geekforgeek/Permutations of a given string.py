#code
def ans1(s, idx, ret):
    if idx == len(s):
        ret.append("".join(s))
        return
    
    for i in range(idx, len(s)):
        s[idx], s[i] = s[i], s[idx]
        ans1(s, idx + 1, ret)
        s[idx], s[i] = s[i], s[idx]


T = int(input())
for _ in range(T):
    s = list(input())
    ret = []
    ans1(s, 0, ret)
    ret.sort()
    print (" ".join(ret))
    
