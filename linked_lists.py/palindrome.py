# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or head.next == None:

            return True
        slow = head
        fast = head
        while fast.next!= None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            def reverse(node):
                prev = None
                curr = node
                while curr:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    currr = next_node
            new_head = reverse(slow.next)
            first =head
            second = new_head
            while second!= None:
                if first.data != second.data:
                    reverse(new_head)
                    return False
                first = first.next
                second = second.next
        reverse(new_head)

        return True