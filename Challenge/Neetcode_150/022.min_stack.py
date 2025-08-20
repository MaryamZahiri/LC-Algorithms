# https://leetcode.com/problems/min-stack/
class Node:
    def __init__(self, val, min_val = float("inf"), pre = None):
        self.value = val
        self.min_val = min_val
        self.pre = pre
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head: self.head = Node(val, val, None)
        else: self.head = Node(val, min(val, self.head.min_val), self.head)

    def pop(self) -> None:
        self.head = self.head.pre
        
    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min_val
"""
2, 3, -1 , min, pop, top, min
head,min,pre
2,2,None

   3,2,2

       -1,-1,3

           -1
               
                head = pre: 3
                    
                     3

                          2   
"""
class MinStackUsual:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
"""
2, 3, -1 , min, pop, top, min
[2,3,-1]
[2,2,-1]
            -1, [2,3],3, 2
                [2,2]
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()