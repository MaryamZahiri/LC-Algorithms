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
### 1. [Traversing all Vertices]()

### 2. Traversing all paths between two vertices vs Shortest Path Between Two Vertices
#### Problem Description
> Example: LeetCode Problem 797 - [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)
- Directed graph: No need to mark as visited node (Only in undirected graph, we mark visited nodes )

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

#### Solution Approaches
- DFS Approach - Depth First Search Algorithm in Graph
- BFS Approach - Breadth-First Search Algorithm in Graph
#### DFS Data Structure 
- adjacency list - Graph model - mapping all nodes to list of the neighbor node
- stack - Top out
- visited/seen
#### BFS Data Structure - Shortest move possible
- adjacency list - Graph model - mapping all nodes to list of the neighbor node 
- Queue - FIFO - First in, First out
- visited/seen
#### DFS Example Explanation
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/825fc46c-9978-4af8-b415-95899545f51e" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9772830e-007a-4644-beb8-b48017e7eb1b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/e6b97c08-e820-4bb5-96cd-3813d521007e" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/eab2f60a-362f-4f63-a06e-9d116f4e4b9a" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/c09a4a10-0242-46f3-b16c-2e4f10ae20a1" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/db65688d-8efd-491d-8a18-031c17f968c0" width="250"><br />

#### BFS Example Explanation
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/e1346d46-25cd-4dfe-bff6-dc4d15ae41ab" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ce7a2fdd-2285-47a1-b06d-1c4ab0046aaf" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a40f78fb-9f90-4a98-b5f2-8987143fcd5d" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/daa7f106-6edf-4ad9-8ac6-2ee3eec9513b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/af83d792-24bb-4a6b-9e1a-3042a41856eb" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/c846f644-c90f-4197-a32a-20417db262e9" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9ab23ac2-e279-4c00-a702-01acab16c34b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/318677e4-c57a-4614-b358-3b19acb62405" width="250"><br />

#### Code Solutions
##### DFS Solution
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
##### BFS Solution
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque()
        path = [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths
```
#### Complexity Analysis
##### DFS Complexity
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/7bf7d544-71d1-4b5c-bf2f-e5645ed3852e" width="460"><br />

##### BFS Complexity
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/f67558cd-8129-4eea-938e-8f2e3681f47b" width="460"><br />



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
[Explore Graph from Leedcode](https://leetcode.com/explore/learn/card/graph/)

[Data Structur](https://www.youtube.com/watch?v=ZdY1Fp9dKzs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=40)