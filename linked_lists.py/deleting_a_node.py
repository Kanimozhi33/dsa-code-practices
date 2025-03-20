# delete the given node, while head is not givrn and the node to be deleted is not the last node.
#return the head of the linked list after deleting the given node.
# '''  
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
         
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return