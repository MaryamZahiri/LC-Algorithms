'''
LIFO: Last In First Out
Time Complexity O(1): a stack limits the insert (push) and remove (pop) operation to only one end of the data structure, i.e., to the top
Python lists are implemented as dynamic arrays
'''
class stack:
    def __init__(self, initList=[]):
        self.stack = initList

    def push(self, element):
        self.stack.append(element)
        return self.stack
    
    def pop(self):
        return self.stack.pop()
    
    def check_stack(self):
        print(self.stack)

    def check_top(self):
        print(self.stack[-1])
    

stack_ds = stack()
stack_ds.push(1)
stack_ds.push(2)
stack_ds.push(3)
stack_ds.check_stack()
# [1,2,3]
stack_removed = stack_ds.pop()
# 3
stack_ds.check_stack()
# [1,2]
stack_ds.check_top()
#  2