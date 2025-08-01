# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n) :
        if not head:
            return None
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head