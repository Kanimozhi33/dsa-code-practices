# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head and head.next == None:
            return None
        slow = head
        fast = head
        prev = None
        while fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = slow.next
        return head