class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA,headB):
        if not headA or not headB:
            return None
        temp1 = headA
        temp2 = headB
        while temp1!= temp2:
            temp1 = temp1.next
            temp2 = temp2.next
            if temp1 == temp2:
                return temp1
            if temp1 == None:
                temp1 = headB
            elif temp2 == None:
                temp2 = headA
        return temp1