import collections
import time

ghist = {}

def swap(brr, i, j, posb):
    posb[brr[i]].remove(i)
    posb[brr[j]].remove(j)
    posb[brr[j]].add(i)
    posb[brr[i]].add(j)
    brr[i], brr[j] = brr[j], brr[i]

def recur_util(arr, brr, posb, index):
    global ghist
    #raw_input()
    #print ghist
    sarr = "".join(arr[index:])
    sbrr = "".join(brr[index:])
    #print "start:"
    #print index, sarr, sbrr, posb
    #if arr == brr:
        #return 0
    
    
    if ghist.has_key(sbrr):
        #print sarr, sbrr, ghist[sbrr]
        return ghist[sbrr]
    '''
    posb = collections.defaultdict(list)
    for i in xrange(len(brr)):
        posb[brr[i]].append(i)
    '''
    gcnt = 0x7fffffff
    for i in xrange(index, len(brr)):
        if brr[i] != arr[i]: # need to swap
            for j in posb[arr[i]]:
                if j < i:
                    continue
                swap(brr, i, j, posb)
                #print "inter:", index, sarr, sbrr, i, j
                tcnt = 1 + recur_util(arr, brr, posb, i + 1)
                swap(brr, i, j, posb)
                gcnt = min(gcnt, tcnt)
            break

    if gcnt == 0x7fffffff:
        gcnt = 0
    ghist[sbrr] = gcnt
    #print "end:"
    #print index, sarr, sbrr, gcnt
    return gcnt

def ans(arr, brr):
    global ghist
    ghist = {}
    if arr == brr:
        return 0
    
    posb = collections.defaultdict(set)
    for i in xrange(len(brr)):
        posb[brr[i]].add(i)
    
    gcnt = 0x7fffffff
    for i in xrange(len(brr)):
        if brr[i] != arr[i]: # need to swap
            for j in posb[arr[i]]:
                if j < i:
                    continue
                swap(brr, i, j, posb)
                tcnt = 1 + recur_util(arr, brr, posb, i + 1)
                #print "first:", tcnt
                swap(brr, i, j, posb)
                gcnt = min(gcnt, tcnt)
            break
    return gcnt

class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        return ans(list(A), list(B))

print "abcdeabcdeabcdeabcde"
print "aaaabbbbccccddddeeee"
A = list("abcdeabcdeabcdeabcde")
B = list("aaaabbbbccccddddeeee")
print ans(A, B)
