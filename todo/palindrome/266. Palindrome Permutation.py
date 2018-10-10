import collections


def ans(s):
    cs = collections.Counter(s)
    oCnt = 0
    for key in cs.keys():
        if cs[key] % 2 != 0:
            oCnt += 1
        if oCnt > 1:
            return False
    return True


# "code" -> False, "aab" -> True, "carerac" -> True
cases = [
    ('code', False),
    ('aab', True),
    ('carerac', True)
]
for case in cases:
    print ans(case[0]) == case[1]

