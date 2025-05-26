/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let less_head = new ListNode(0);
    let less_tail = less_head;
    let greater_head = new ListNode(0);
    let greater_tail = greater_head;



    while (head != null ){
        if (head.val < x){
            less_tail.next = head
            less_tail = head

        }
        else{
            greater_tail.next = head
            greater_tail = head
        }
        head = head.next
    };

    greater_tail.next = null;
    less_tail.next = greater_head.next;
    return less_head.next;

};