
class Solution {
    inorder(root) {
        //your code goes here
        if (!root) {
            return [];
        }
        let stack = [];
        let result = [];
        let current = root;
        
        while (current !== null || stack.length > 0) {
            // Go as far left as possible
            while (current !== null) {
                stack.push(current);
                current = current.left;
            }
            
            // Process the leftmost node
            current = stack.pop();
            result.push(current.val);
            
            // Move to the right subtree
            current = current.right;
        }
        
        return result;
    }
}
