# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def ans(head):
    length = 0
    tmp = head
    while tmp != None:
        tmp = tmp.next
        length += 1
        
    if length == 1:
        return True
    
    mid = length // 2
    pre = None
    left = None
    right = head
    while mid != 0:
        left = right
        right = right.next
        left.next = pre
        pre = left
        mid -= 1
    
    if length % 2 != 0:
        right = right.next
    
    mid = length // 2
    for i in xrange(mid):
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return ans(head)
        
