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

## Graph Algorithm
### 1. Traversing all Vertices
#### Problem Description
> Example: LeetCode Problem 1971 - [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. You want to determine if there is a valid path that exists from vertex source to vertex destination. Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
#### Solution Approaches
- DFS Approach - Depth First Search Algorithm in Graph
- BFS Approach - Breadth-First Search Algorithm in Graph
#### DFS Data Structure 
- adjacency list - mapping all nodes to list of the neighbor node
- stack
- visited/seen
#### BFS Data Structure 
- adjacency list
- Queue
- visited/seen
#### DFS Example Explanation
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/71e6117d-d6c9-4ab4-8284-231935e3d02f" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/cc8797f9-c400-40ea-a376-0918fa700733" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ab60b9d7-19a1-4657-8966-376587a5b1dc" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/600064aa-eb86-46c3-a601-1e47a5b16e7e" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/d9d90630-d145-4d65-a974-638b2a9bc6ec" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/840450ee-4346-4bf4-b442-af3d7a41db56" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/4efdab4f-7b54-479c-a4ec-7e4ec4e9eaa6" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/b4d38539-e41f-437a-807d-802bb3dd77c1" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/26c6954a-91b2-4bc1-8eef-23dd0e69d7f2" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/3fe02044-63ca-4d95-aa1f-cd21a22eef72" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ad804820-dba8-4a0e-9931-d46b2902d206" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/97027df0-bd56-4684-b520-2a4c91c317a1" width="250"><br />

#### BFS Example Explanation
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/97027df0-bd56-4684-b520-2a4c91c317a1" width="460"><br />

#### Code Solutions
##### DFS Solution
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

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/81a0ceb3-50b5-47fc-a7c6-28f1f86e5dad" width="460"><br />

### 2. Traversing all paths between two vertices
> Example: LeetCode 797 - All Paths From Source to Target
- Directed graph: No need to mark as visited node (Only in undirected graph, we mark visited nodes )
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/db65688d-8efd-491d-8a18-031c17f968c0" width="460"><br />

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            next_nodes = graph[node]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        paths = []
        path = []
        if not graph or len(graph) == 0:
            return paths
        dfs(0)
        return paths
```
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/7bf7d544-71d1-4b5c-bf2f-e5645ed3852e" width="460"><br />

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

[Data Structur](https://www.youtube.com/watch?v=ZdY1Fp9dKzs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=40)