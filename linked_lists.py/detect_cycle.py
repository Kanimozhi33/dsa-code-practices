class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop = True
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
                
        return None