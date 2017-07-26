import sys
from collections import defaultdict
from itertools import chain

n, q = map(int, raw_input().split())
arr = list(map(int, raw_input().strip().split(' ')))

def stat(pos_x, pos_y):
    global n
    L = [(i, 1) for i in pos_x]
    L.extend([(j, -1) for j in pos_y])
    L.sort()
    
    freq = defaultdict(int)
    i_prev = 0
    s = 0
    for i, f in chain(L, [(n, 0)]):
        freq[s] += i - i_prev
        s += f
        i_prev = i 

    return freq[0] + sum([n*(n-1)//2 for n in freq.values()])

n = len(arr)
cnt = n*(n + 1)//2

queried_values = set([])
queries = [None]*q
for idx in range(q):
    x, y = map(int, raw_input().split())
    
    queried_values.add(x)
    queried_values.add(y)
    queries[idx] = (x, y)

positions = {v: [] for v in queried_values}
for i, a in enumerate(arr):
    if a in queried_values:
        positions[a].append(i)
for a in positions:
    positions[a].sort()
    
elems = set(arr)
        
results = {}
for x, y in queries: 
    if x == y:
        print(cnt)
        continue
        
    x_in_arr = x in elems
    y_in_arr = y in elems
    
    if not x_in_arr and not y_in_arr:
        print(cnt)
        continue
        
    key_x = x if x_in_arr else -1
    key_y = y if y_in_arr else -1
            
    key = (min(key_x, key_y), max(key_x, key_y))
        
    val = results.get(key, None)    
    if val is None:       
        val = stat(positions[x], positions[y])
        results[key] = val
        
    print(val)

def main():
    n, q = map(int, raw_input().split())
    arr = list(map(int, raw_input().strip().split(' ')))
    pass

if __name__ == "__main__":
    main()
