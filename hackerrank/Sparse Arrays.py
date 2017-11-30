# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

ns = int(raw_input())
cnss = collections.defaultdict(int)
for i in xrange(ns):
    cnss[raw_input().strip()] += 1

qs = int(raw_input())
for i in xrange(qs):
    print cnss[raw_input().strip()]
