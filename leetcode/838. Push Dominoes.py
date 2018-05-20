
def ans(dominoes):
    ret = [(".", 0)] * len(dominoes)
    for i in xrange(len(dominoes)):
        if dominoes[i] == "L" or dominoes[i] == "R":
            ret[i] = (dominoes[i], 0)

    for i in xrange(len(dominoes)):
        if dominoes[i] == ".":
            continue

        if dominoes[i] == "L":
            j = i - 1
            d = 1
            while j > -1:
                if ret[j][0] == "L":
                    break

                if ret[j][0] == "R" and ret[j][1] < d:
                    break

                if ret[j][0] == "R" and ret[j][1] == d:
                    ret[j] = (".", d)
                    break

                ret[j] = ("L", d)
                j -= 1
                d += 1
        else:
            j = i + 1
            d = 1
            while j < len(dominoes):
                if ret[j][0] == "R":
                    break

                if ret[j][0] == "L" and ret[j][1] < d:
                    break

                if ret[j][0] == "L" and ret[j][1] == d:
                    ret[j] = (".", d)
                    break

                ret[j] = ("R", d)
                j += 1
                d += 1
        
    #print ret
    return "".join([ x[0] for x in ret ])

dominoes = ".L.R...LR..L.."
print (ans(dominoes))

dominoes = "RR.L"
print (ans(dominoes))
