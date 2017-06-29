import sys

# pattern : 10+1

def start_state(c, pre):
    if c == "1":
        pre.append(c)
        return (0, "one")
    else:
        del pre[:]
        return (1, "start")

def one_state(c, pre):
    if c == "1":
        return (1, "one")
    elif c == "0":
        pre.append(c)
        return (0, "zero")
    else:
        return (0, "start")

def zero_state(c, pre):
    if c == "0":
        pre.append(c)
        return (1, "zero")
    elif c == "1":
        return (0, "end")
    else:
        return (0, "start")

def end_state(c, pre):
    pre.append(c)
    print "".join(pre)
    return (1, "start")

def main(s):
    state = "start"
    cnt = 0 
    pre = []
    while cnt < len(s):
        func = getattr(sys.modules[__name__], "%s_state"%state)
        step, state = func(s[cnt], pre)
        cnt += step

if __name__ == "__main__":
    main("100001abc101")