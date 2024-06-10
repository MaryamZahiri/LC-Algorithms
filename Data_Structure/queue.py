'''
FIFO: First In First Out
limits the insertion and removal of elements to specific ends of the data structure
Insertion operation occurs at the tail of the list, while the deletion operation occurs at the head of the list.
The problem still remains, since popping from the front of the list will be O(N)
 as everything to the right must shift to the left.
'''
class queue:
    def __init__(self, initList=[]):
        self.queue = initList

    def enqueue(self, element):
        self.queue.append(element)
        return self.queue
    
    def dequeue(self):
        return self.queue.pop(0)

    def checkQueue(self):
        print(self.queue)

    def checkHead(self):
        print(self.queue[0])

    def checkTail(self):
        print(self.queue[-1])

queue_ds = queue()
queue_ds.enqueue(1)
queue_ds.enqueue(2)
queue_ds.enqueue(3)
queue_ds.checkQueue()
# [1,2,3]
queue_ds.dequeue()
queue_ds.checkQueue()
# [2,3]
queue_ds.checkHead()
# 2
queue_ds.checkTail()
# 3