# 2. Graph Algorithm - Traversing all paths between two vertices vs Shortest Path Between Two Vertices
This pattern is efficient for solving problems involving finding all paths between two vertices in a ```directed acyclic graph```, allowing for the exploration of all possible paths from the source to the target vertex.

# LeetCode Problem 797: [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)

## Problem Description
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

## Solution Approaches
> Directed graph: No need to mark as visited node (Only in undirected graph, we mark visited nodes )

- DFS Approach - Depth First Search Algorithm in Graph
- BFS Approach - Breadth-First Search Algorithm in Graph

### DFS Algorithm
The DFS approach is particularly useful for problems that require exploring all possible paths or when the solution involves finding a path or a cycle in a graph.

Algorithm Pattern: DFS for Finding All Paths Between Two Vertices

1. Initialization
    - Purpose: Set up the necessary data structures and prepare the graph for traversal.
    - Steps:
        - Initialize a list ```paths``` to store all valid paths from the source to the target.
        - Initialize a list ```path``` to keep track of the current path being explored.
2. DFS Function
    - Purpose: Explore the graph by going as deep as possible along each branch before backtracking.
    - Steps:
        - Define a recursive function that takes the current node as input.
        - Append the current node to the path list.
        - Check if the current node is the target vertex. If so, add the current path to the paths list.
        - For each neighbor of the current node, recursively call the DFS function on the neighbor.
        - After exploring all neighbors, remove the current node from the path list to backtrack.
3. Main Function
    - Purpose: Initiate the DFS traversal from the source vertex.
    - Steps:
        - Call the DFS function with the source vertex as the starting point.
        - The DFS function will recursively visit all reachable nodes from the source vertex, exploring all possible paths to the target vertex.
        - Return the list of all valid paths.

### BFS Algorithm - Shortest move possible - It is not recursive algorithm, it is itterative
Breadth-First Search (BFS) approach to explore all possible paths from the source vertex to the target vertex in a directed acyclic graph (DAG)

Algorithm Pattern: BFS for Finding All Paths Between Two Vertices
1. Initialization
    - Purpose: Prepare the necessary data structures for the algorithm.
    - Steps:
        - Create a queue to keep track of paths to explore.
        - Initialize a list paths to store all valid paths from the source to the target.
2. BFS Function
    - Purpose: Perform a breadth-first search on the graph to explore all possible paths from the source to the target.
    - Steps:
        - Enqueue the initial path, which contains only the source vertex, into the queue.
        - While the queue is not empty, dequeue a path.
        - For each neighbor of the last vertex in the dequeued path, create a new path by appending the neighbor to the copy of dequeued path. Enqueue this new path into the queue.
        - Check if the last vertex in the dequeued path is the target vertex. - If so, add the new path to the paths list.
3. Main Function
    - Purpose: Initiate the BFS process to find all paths from the source to the target.
    - Steps:
        - Call the BFS function, which will iteratively visit all reachable paths from the source vertex to the target vertex.
        - Return the list of all valid paths.

## Example Description
### DFS Example Description
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/825fc46c-9978-4af8-b415-95899545f51e" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9772830e-007a-4644-beb8-b48017e7eb1b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/e6b97c08-e820-4bb5-96cd-3813d521007e" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/eab2f60a-362f-4f63-a06e-9d116f4e4b9a" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/c09a4a10-0242-46f3-b16c-2e4f10ae20a1" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/db65688d-8efd-491d-8a18-031c17f968c0" width="250"><br />


### BFS Example Description
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/e1346d46-25cd-4dfe-bff6-dc4d15ae41ab" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ce7a2fdd-2285-47a1-b06d-1c4ab0046aaf" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a40f78fb-9f90-4a98-b5f2-8987143fcd5d" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/daa7f106-6edf-4ad9-8ac6-2ee3eec9513b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/af83d792-24bb-4a6b-9e1a-3042a41856eb" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/c846f644-c90f-4197-a32a-20417db262e9" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9ab23ac2-e279-4c00-a702-01acab16c34b" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/318677e4-c57a-4614-b358-3b19acb62405" width="250"><br />

## Python Code
### DFS Solution
Inputs
```python
# Example: Graph as a adjacency list
# Index -> [neighbor 1, neighbor 2]
graph = [[1,2],[3],[3],[]]
```
Solution Code 1 - dfs
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)

            # Check if we have reached the target node.
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
Solution Code 2 - dfs
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        paths = []

        stack = []

        def dfs():
            stack = [path]
            while stack:
                current_path = stack.pop()
                current_node = current_path[-1]

                for neighbor in graph[current_node]:
                    new_path = current_path + [neighbor]

                    if neighbor == len(graph) - 1: 
                        paths.append(new_path)
                    else:
                        stack.append(new_path)

        dfs()
        return paths
```
### BFS Solution
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        paths = []
        queue = deque()
        queue.append(path)

        if not graph or len(graph) == 0:
            return paths

        def bfs():
            while queue:
                current_path = queue.popleft()
                current_node = current_path[-1]

                for neighbor in graph[current_node]:
                    # new_path = current_path + [neighbor]
                    # OR
                    new_path = current_path.copy()
                    new_path.append(neighbor)

                    if neighbor == len(graph) - 1:
                        paths.append(new_path)
                    else:
                        queue.append(new_path)

        bfs()
        return paths
```
## Complexity Analysis
- Time complexity : 
    - DFS Time Complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph. This is because each vertex and edge is visited exactly once.

    - BFS Time Complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph. This is because each vertex and edge is visited exactly once.

- Space complexity : 
    - DFS Space Complexity - O(V), where V is the number of vertices in the graph. This accounts for the space required for the path list and the call stack in the worst case.

    - BFS Space Complexity - O(V), where V is the number of vertices in the graph. This is due to the space required for the queue and the paths list in the worst case.