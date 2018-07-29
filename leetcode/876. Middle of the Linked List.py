# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def ans(head):
    cnt = 0
    tmp = head
    while tmp != None:
        cnt += 1
        tmp = tmp.next
    
    mid = (cnt // 2)

    tmp = head
    while mid != 0:
        tmp = tmp.next
        mid -= 1
    
    return tmp

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return ans(head)
        
