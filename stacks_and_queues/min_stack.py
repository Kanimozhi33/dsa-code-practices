class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:

            top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
            


    def top(self) -> int:
        if self.stack:

            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
    

    # javascript code:
# class MinStack {
#    constructor() {
#        this.stack = []; // Main stack to store elements
#        this.minStack = []; // Stack to keep track of minimum elements
#    }
#
#    push(val) {
#        this.stack.push(val); // Push the value onto the main stack
#       // If the minStack is empty or the new value is less than or equal to the current minimum, push it onto the minStack
#        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
#            this.minStack.push(val);
#        }
#    }
#
#    pop() {
#        if (this.stack.length > 0) {
#            const top = this.stack.pop(); // Pop the top element from the main stack
#            // If the popped element is the current minimum, pop it from the minStack as well
#            if (top === this.minStack[this.minStack.length - 1]) {
#                this.minStack.pop();
#            }
#        }
#    }
#
#    top() {
#        if (this.stack.length > 0) {
#            return this.stack[this.stack.length - 1]; // Return the top element of the main stack
#        } else {
#            return null; // Return null if the stack is empty
#        }
#    }
#
#    getMin() {
#        if (this.minStack.length > 0) {
#            return this.minStack[this.minStack.length - 1]; // Return the top element of the minStack (minimum element)
#        } else {
#            return null; // Return null if the minStack is empty
#        }
#        }
#    }
#

