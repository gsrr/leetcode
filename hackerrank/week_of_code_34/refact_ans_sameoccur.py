import sys
from collections import defaultdict
from itertools import chain

def stat(pos_x, pos_y, n):
    L = [(i, 1) for i in pos_x]
    L.extend([(j, -1) for j in pos_y])
    L.sort()
    
    freq = defaultdict(int)
    i_prev = 0
    s = 0
    for i, f in chain(L, [(n, 0)]):
        print i,f
        freq[s] += i - i_prev
        s += f
        i_prev = i 
    
    print freq
    print sum([n*(n-1)//2 for n in freq.values()])
    return freq[0] + sum([n*(n-1)//2 for n in freq.values()])


def same_xy(n):
    cnt = n*(n + 1)//2 # total number of sub array
    return cnt

def notexists_xy(n):
    cnt = n*(n + 1)//2 # total number of sub array
    return cnt

def is_xy_notexists(positions, x, y):
    if len(positions[x]) == 0 and len(positions[y]) == 0:
        return True
    return False

def main():
    n, q = map(int, raw_input().split())
    arr = list(map(int, raw_input().strip().split(' ')))

    cnt = n*(n + 1)//2 # total number of sub array

    queried_values = set([])
    queries = [None]*q
    for idx in range(q):
        x, y = map(int, raw_input().split())
        
        queried_values.add(x)
        queried_values.add(y)
        queries[idx] = (x, y)

    # find all position for every query number
    positions = {v: [] for v in queried_values}
    for i, val in enumerate(arr):
        if val in queried_values:
            positions[val].append(i)
    
    for a in positions:
        positions[a].sort()
        
    elems = set(arr)
    ret = {}
    for x, y in queries: 
        print "=" * 5 , x,y, "=" * 5
        if x == y:
            print same_xy(n)
        elif is_xy_notexists(positions,x, y): 
            print notexists_xy(n)
        else:     
            x_in_arr = x in elems
            y_in_arr = y in elems
            key_x = x if x_in_arr else -1
            key_y = y if y_in_arr else -1
                    
            key = (min(key_x, key_y), max(key_x, key_y))
                
            if ret.has_key(key) == False:
                ret[key] = stat(positions[x], positions[y], n)
                
            print(ret[key])

if __name__ == "__main__":
    main()
