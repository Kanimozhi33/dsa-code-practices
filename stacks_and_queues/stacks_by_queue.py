import collections
from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1,self.queue2 = self.queue2,self.queue1

    def pop(self) -> int:
        if not self.queue1:
            return -1
        return self.queue1.popleft()

    def top(self) -> int:
        if not self.queue1:
            return -1
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1
    
# javascript code:
# class MyStack {
#     constructor() {   
#        this.queue1 = []; // Queue to hold the elements
#        this.queue2 = []; // Queue to reverse the order of elements
#     }
#     push(x) {
#        this.queue2.push(x);
#        while (this.queue1.length > 0) {
#            this.queue2.push(this.queue1.shift());
#        }
#        this.queue1 = this.queue2;
#        this.queue2 = [];
#     }
#     pop() {
#        if (this.queue1.length === 0) {
#            return -1;
#        }
#        return this.queue1.shift();
#     }
#     top() {
#        if (this.queue1.length === 0) {
#            return -1;
#        }
#        return this.queue1[0];
#     }
#     empty() {
#        return this.queue1.length === 0;
#     }
# }
        