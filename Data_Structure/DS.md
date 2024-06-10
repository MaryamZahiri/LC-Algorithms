Stack: LIFO (last in first out)

Queue: FIFO (First in first out)

![Stack vs Queue](https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/02c1b59e-195a-4a95-8f81-29f58bc12841)

>> Notes
Queue Mistake: using lists over the more efficient deque in an interview setting where time complexity is important is not ideal.

The problem remains, since popping from the front of the list and inserting an element at the front of a list will be O(N) as everything to the right must shift to the left.