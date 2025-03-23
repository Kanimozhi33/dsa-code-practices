
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


def insertion(self,new_data,head):
    new_node = Node(new_data)
    if not self.head:
        self.head = new_node

    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

    return self.head

# def print_list(self,node):
#     while node:
#         print(node.data)    
#         last = node
#         node = node.next        
#     print("\n")
#     while last:
#         print(last.data)
#         last = last.prev
#     print("\n")
