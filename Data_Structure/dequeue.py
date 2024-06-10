'''
Deque: Double Ended Queue
Time Complexity: insert and remove from both ends in O(1) time
'''
from collections import deque

queue = deque([])
queue.appendleft(3)
queue.appendleft(2)
queue.appendleft(1)
print(queue)
# [1,2,3]
queue.pop()
print(queue)
# [1,2]
queue.popleft()
print(queue)
# [2]