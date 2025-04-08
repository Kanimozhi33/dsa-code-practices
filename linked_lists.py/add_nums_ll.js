/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    const dummyNode = new ListNode(-1);
    let curr = dummyNode;
    let t1 = l1;
    let t2 = l2;
    let carry = 0;
    while (t1 !== null || t2 !== null) {
        let sum = carry;
        if (t1) {
            sum += t1.val;
            t1 = t1.next;}

        if (t2) {
            sum += t2.val;
            t2 = t2.next;
        }
        const newNode = new ListNode(sum % 10);
        carry = Math.floor(sum/10);
        curr.next = newNode;
        curr = curr.next;
        // if (t1) {t1 = t1.next}
        // if(t2) {t2 = t2.next}

    }
    if (carry >0) {
        const newNode = new ListNode(carry);
        curr.next = newNode;

    }
    return dummyNode.next;
};