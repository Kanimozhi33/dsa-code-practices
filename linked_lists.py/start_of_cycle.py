class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False