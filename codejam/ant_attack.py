def recut_util(rarr, hist, max_weight):
    n = len(rarr)
    key = (n, max_weight)
    if hist.has_key(key):
        return hist[key]
    max_len = 0
    for i in xrange(len(rarr)):
        if rarr[i] > max_weight:
            continue
        w1 = rarr[i] * 6
        w2 = max_weight - rarr[i]
        tmp_len = 1 + recut_util(rarr[i + 1:], hist, min(w1, w2))
        if tmp_len > max_len:
            max_len = tmp_len
    hist[key] = max_len
    return max_len


def ant_attack(arr):
    rarr = arr[::-1]
    max_len = 0
    hist = {}
    for i in xrange(len(rarr)):
        max_weight = 6 * rarr[i]
        tmp_len = 1 + recut_util(rarr[i + 1:], hist, max_weight)
        if tmp_len > max_len:
            max_len = tmp_len
    return max_len

def main():
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        arr = list(map(int, raw_input().strip().split()))
        print "Case #%d: %s"%(i+1, ant_attack(arr))

if __name__ == "__main__":
    main()
