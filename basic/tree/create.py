import main

def get_val(ts, i):
    print "get_val"
    ret = []
    j = i
    while j < len(ts):
        if ts[j] == "(":
            break
        ret.append(ts[j])
        j += 1
    return (int("".join(ret)), j)

def get_left(ts, i):
    print "get_left"
    ret = []
    ret.append(ts[i])
    j = i + 1
    cnt = 1
    while j < len(ts) and cnt != 0:
        if ts[j] == ")":
            cnt -= 1
        elif ts[j] == "(":
            cnt += 1
        ret.append(ts[j])
        j += 1
    return ("".join(ret), j)

def get_tree(ts):
    i = 0
    lts, rts = None, None
    state = "get_val"
    while i < len(ts):
        if state == "get_val":
            val, j = get_val(ts, i)
            i = j
            state = "get_left"

        elif state == "get_left":
            lts, j = get_left(ts, i)
            i = j
            state = "get_right"
        elif state == "get_right":
            rts, j = get_left(ts, i)
            i = j
            state = "get_right"
    print val, lts[1:-1], rts[1:-1]
        
def ans(ts):
    val, left, right = get_tree(ts)
    return ""





if __name__ == "__main__":
    main.main(ans)
