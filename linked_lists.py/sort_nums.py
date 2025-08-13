class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

class Solution:

    def sort_nums(self,head):
        if not head or not head.next:
            return head
        dummy_node0 = Node(-1)
        dummy_node1 = Node(-1)

        dummy_node2 = Node(-1)
        zero = dummy_node0
        one = dummy_node1
        two = dummy_node2

        temp = head
        while temp:
            if temp.data == 0:
                zero.next = temp

                zero = temp
                temp = temp.next
            elif temp.data == 1:
                one.next = temp
                one = temp
                temp = temp.next

            else:
                two.next = temp
                two = temp
                temp = temp.next
        zero.next = dummy_node1.next
        one.next = dummy_node2.next
        two.next = None
        new_head = dummy_node0.next
        return new_head
    
    # optimal approach
        if not head or not head.next:
            return head
        count = [0,0,0]
        temp = head
        while temp:
            count[temp.data] +=1
            temp = temp.next
        
        temp = head
        for i in range(3):
            while count[i] >0:
                temp.data = i
                temp = temp.next
                count[i] -=1
        return head
    