class Solution:
    def isValid(self, s):
        stack = []
        dict_1 = {")":"(", "]":"[","}":"{"}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if stack:

                    popped = stack.pop()
                    if dict_1[i] != popped :
                        return False
                    
                else:
                    return False
        return not stack
    

    # javascript code:
    # class Solution {
    #    isValid(s) {
    #        const stack = []; // Initialize an empty stack
    #        const dict = {')': '(', ']': '[', '}': '{'}; // Mapping of closing to opening brackets
    #        for (let char of s) {
    #            if (char === '(' || char === '{' || char === '[') {
    #                stack.push(char); // Push opening brackets onto the stack
    #            } else {
    #                if (stack.length) {
    #                    const popped = stack.pop(); // Pop the top element from the stack
    #                    if (dict[char] !== popped) {
    #                        return false; // Mismatch found
    #                    }
    #                } else {
    #                    return false; // Stack is empty but closing bracket found
    #                }
    #            }
    #        }
    #        return stack.length === 0; // Return true if stack is empty, false otherwise
    #    }
    # }
#