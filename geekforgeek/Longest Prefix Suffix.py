#code

def prefix_func(s, reverse = False):
    ret = {}
    pf = [-1] * len(s)
    for i in range(1, len(s)):
        j = pf[i - 1]
        while j > -1 and s[i] != s[j + 1]:
            j = pf[j]
        
        if s[i] == s[j + 1]:
            pf[i] = j + 1
            if reverse:
                ret[s[0:j + 2][::-1]] = True
            else:
                ret[s[0:j + 2]] = True
    #print(pf)
    return ret

def suffix_func(s):
    pass

def main():
    num = int(input())
    for i in range(num):
        s = input()
        pf = prefix_func(s)
        sf = prefix_func(s[::-1], True)
        #print(pf)
        #print(sf)
        max_len = 0
        for key in pf.keys():
            if len(key) <= max_len:
                continue
            else:
                if key in sf:
                    max_len = len(key)
        print (max_len)
        
if __name__ == "__main__":
    main()
