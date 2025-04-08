class Node:
    def __init__(self, x):
        self.val = x
        self.next = None



def helper(temp):
    if not temp:
        return 1
    carry = helper(temp.next)
    temp.data += carry
    if temp.data < 10:
        return 0
    else:
        temp.data = 0
        return 1

def add_one(head):
    carry = helper(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        head = newNode
    return newNode