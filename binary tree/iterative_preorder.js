
class Solution {
    preorder(root) {
        //your code goes here
        if (!root){
            return [];
        }
        let stack = [root];
        let result = [];
        while (stack.length >0){
            let node = stack.pop()
            result.push(node.data);
            if (node.right){
                stack.push(node.right);
            };
            if (node.left){
                stack.push(node.left)
            };
        }
        return result;
    }
}