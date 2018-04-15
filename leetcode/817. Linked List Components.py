# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import collections

def ans1(head, G):
    cg = collections.Counter(G)
    cnt = 0
    p = head
    tcnt = 0
    while p != None:
        #print p.val
        if cg.has_key(p.val) == False:
            if tcnt != 0:
                cnt += 1
            tcnt = 0
        else:
            tcnt += 1
            
        p = p.next
    if tcnt != 0:
        cnt += 1
    return cnt

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        return ans1(head, G)    
