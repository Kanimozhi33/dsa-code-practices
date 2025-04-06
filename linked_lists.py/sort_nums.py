def sort_nums(head):
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