

def ans1(rec1, rec2):
    print rec1, rec2
    if rec1 == rec2:
        return True

    pts = [(rec1[0], rec1[1]), (rec1[2], rec1[1]), (rec1[2], rec1[3]), (rec1[0], rec1[3])]
    for p in pts:
        if p[0] > rec2[0] and p[0] < rec2[2]:
            if p[1] > rec2[1] and p[1] < rec2[3]:
                return True
    return False

def check_rect(rec1, rec2):
    x11 = rec1[0]
    x12 = rec1[2]
    x21 = rec2[0]
    x22 = rec2[2]
    if x21 >= x12:
        return False
    y11 = rec1[1]
    y12 = rec1[3]
    y21 = rec2[1]
    y22 = rec2[3]
    if y21 >= y12:
        return False
    if y22 <= y11:
        return False

    return True

def ans(rec1, rec2):
    x11 = rec1[0]
    x12 = rec1[2]
    x21 = rec2[0]
    x22 = rec2[2]
    if x11 < x21:
        return check_rect(rec1, rec2)
    else:
        return check_rect(rec2, rec1)

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print ans(rec1, rec2)

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print ans(rec1, rec2)


