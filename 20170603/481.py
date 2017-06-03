import time


mgs = "122"

c = "2"
i = 2
while len(mgs) < 100000:
    if c == "2":
        c = "1"
    else:
        c = "2"
    mgs += c * int(mgs[i])
    i += 1
    time.sleep(1)
    print mgs
