# Graph
Non-linear data structure
Nodes and edges - no rules
## Types of “graphs”
- Undirected graphs
> G = {V, E}
> Facebook Network
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/290ca436-9b2c-4597-b44e-0ed37f7297ca" width="460">

- Directed graphs
> G = (V, E)
> Google Webs
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9071661c-7c2d-484d-bff0-97df650912e0" width="460">

- Weighted graphs
> Road map network (weight = distances)
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/32e6a102-1577-493c-9035-88829b986e3e" width="460">

### Properties of Graph
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/289568f3-0c49-4315-8124-c69c0952a3cf" width="460">

## Graph implementation
1. Edge List
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/7892e93f-14c7-4ba2-9433-522eebf7d455" width="460">

2. Adjancy Matrix
3. Adjancy List

## DFS
### 1. Traversing all Vertices
- adjacency list
- stack
- visited/seen
> Example: LeetCode 1971 - Find if Path Exists in Graph - DFS
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        
        stack = [start]
        seen = set()
        
        while stack:
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False
```
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/97027df0-bd56-4684-b520-2a4c91c317a1" width="460"><br />
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/81a0ceb3-50b5-47fc-a7c6-28f1f86e5dad" width="460"><br />

### 2. Traversing all paths between two vertices
> Example: General dfs
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/2d2f9fc0-1f46-4785-b330-ba6db5e74dcc" width="460"><br />
> Example: Compare dfs with stack and without it
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/d0ddfa33-07be-4997-bbad-1cc846fd7892" width="460"><br />
> Example: Compare preorder vs postorder
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ebb5e211-c8f9-40ac-ae02-51ae5c610a74" width="460"><br />

## BFS
> Example: General bfs
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/6b0a76fd-1ccb-404b-bd03-52b6ecc0e1b1" width="460"><br />

## Sources
[Explore Graph](https://leetcode.com/explore/learn/card/graph/)
[Explore Graph](https://www.youtube.com/watch?v=ZdY1Fp9dKzs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=40)