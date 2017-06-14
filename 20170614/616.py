
def ans(s, d):
    print s, d
    for ds in d:
        print s.find(ds)


s = "aaabbcc"
d = ["aaa","aab","bc"]
print ans(s, d)
