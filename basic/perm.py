import itertools

arr = range(1, 6)
it = itertools.permutations(arr)
for line in it:
    print line
