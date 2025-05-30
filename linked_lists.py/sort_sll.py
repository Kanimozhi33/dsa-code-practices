# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        def mid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Split the list into two halves
        middle = mid(head)
        left = head
        right = middle.next
        middle.next = None

        # Recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge two sorted lists
        def mergesort(list1, list2):
            dummyNode = ListNode(-1)
            temp = dummyNode
            while list1 and list2:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            if list1:
                temp.next = list1
            else:
                temp.next = list2
            return dummyNode.next

        return mergesort(left, right)