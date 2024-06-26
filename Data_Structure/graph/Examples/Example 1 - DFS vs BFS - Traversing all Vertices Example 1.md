# 1. Graph Algorithm - Traversing all Vertices
These patterns provide a structured approach to traversing all vertices in a graph using DFS and BFS. 

DFS is particularly useful for problems that 
- require exploring all possible paths or 
- when the solution involves finding a path or 
- when the solution involves finding a cycle in a graph. 

BFS, on the other hand, is ideal for problems that involve 
- finding the shortest path or 
- when the graph is unweighted

# LeetCode Problem 1971: [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

## Problem Description
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. You want to determine if there is a valid path that exists from vertex source to vertex destination. Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

## Solution Approaches
- DFS Approach - Depth First Search Algorithm in Graph
- BFS Approach - Breadth-First Search Algorithm in Graph
### DFS Algorithm
> Data Structure:

    Adjacency list - Graph model - mapping all nodes to list of the neighbor node

    Stack - A Last-In-First-Out (LIFO) Structure - Pop Top element
    
    Visited/seen

Algorithm Pattern: DFS for Traversing All Vertices Using a Stack

1. Initialization
    - Purpose: Set up the necessary data structures and prepare the graph for traversal.
    - Steps:
        - Create an ```adjacency list``` or matrix to represent the graph.
        - Initialize a ```stack``` to keep track of nodes to visit next. Push the starting node onto the stack.
        - Initialize a set or list to keep track of ```visited/seen``` nodes. Starting visited is the starting node.
2. DFS Function
    - Purpose: Explore the graph by going as deep as possible along each branch before backtracking, using a stack instead of recursive calls.
    - Steps:
        - While the stack is not empty, pop a node from the stack.
        - Check if we reach to the end node
        - For each neighbor of the current node, if the neighbor has not been visited, push it onto the stack.
        - And mark the node as visited.
3. Main Function
    - Purpose: Initiate the DFS traversal from a starting node.
    - Steps:
        - Call and return the DFS function with the starting node.
        - The DFS function will iteratively visit all reachable nodes from the starting node using the stack.

### BFS Algorithm - Shortest move possible - It is not recursive algorithm, it is itterative
> Data Structure:
    
    Adjacency list - Graph model - mapping all nodes to list of the neighbor node 

    Queue - A First-In-First-Out (FIFO) structure

    Visited/seen

1. Initialization
    - Purpose: Set up the necessary data structures and prepare the graph for traversal.
    - Steps:
        - Create an ```adjacency list``` or matrix to represent the graph.
        - Initialize a ```queue``` to keep track of nodes to visit next.
        - Initialize a ```set``` or list to keep track of visited nodes.
2. BFS Function
    - Purpose: Explore the graph by visiting all the neighbors of the current node before moving on to their neighbors.
    - Steps:
        - Define a function that iterates over the nodes in the queue.
        - Dequeue a node from the queue.
        - Check if we have reached the target node.
        - For each neighbor of the dequeued node, if the neighbor has not been visited, enqueue it and mark it as visited.
3. Main Function
    - Purpose: Initiate the BFS traversal.
    - Steps:
        - Call the BFS function, which will iteratively visit all reachable nodes from the starting node in a breadthward manner.

## Example Description
### DFS Example Description
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

### BFS Example Description
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/19282abf-33b1-4c62-936e-b691a805072c" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/b5f25d2c-f8a5-4574-9238-5913e6045578" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/d1e37d13-3ae8-4f31-9463-1352d5bca3c2" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/2c19b4fb-063e-43fb-8a91-3fc615cda7a1" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/4dea6c3f-47c3-4aa5-bd31-be8c129c710f" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a6ac1ee8-bd74-47ed-9749-832ba00e7714" width="250">
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/3427bb86-658e-4bc2-9310-277d7c13ed5e" width="250"><br />

## Python Code
Inputs
```python
# edges -> [node, neighbor]
edges = [[0,1],[1,2],[2,0]]
n = 3
source = 0
destination = 2
```
Adjacency List
```python
# index -> [neighbor 1, neighbor 2]
adjacency_list = [[1,2],[0,2],[0,1]]
```
### DFS Solution
Solution Code 1
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]
        for node, neighbor in edges:
            adjacency_list[node].append(neighbor)
            adjacency_list[neighbor].append(node)

        seen = set([source])
        stack = [source]

        def dfs(): 
            while stack:
                # Get the current node.
                node = stack.pop()
                
                # Check if we have reached the target node.
                if node == destination: 
                    return True

                # Add all neighbors to the stack.
                for neighbor in adjacency_list[node]:
                    # Check if we've already visited this neighbor.
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)

            # Our stack is empty and we did not reach the end node.
            return False

        return dfs()
```
Solution Code 2
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]
        for node, neighbor in edges:
            adjacency_list[node].append(neighbor)
            adjacency_list[neighbor].append(node)

        seen = set()
        stack = [source]

        def dfs(): 
            while stack:
                # Get the current node.
                node = stack.pop()
                
                # Check if we have reached the target node.
                if node == destination: 
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

        return dfs()
```
### BFS Solution
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]
        for node, neighbor in edges:
            adjacency_list[node].append(neighbor)
            adjacency_list[neighbor].append(node)
            
        seen = set([source])
        queue = collections.deque([source])

        def bfs(): 
            while queue:
                # Get the current node.
                node = queue.popleft()
                
                # Check if we have reached the target node.
                if node == destination: 
                    return True

                # Add all neighbors to the stack.
                for neighbor in adjacency_list[node]:
                    # Check if neighbor has been added to the queue before.
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)

            # Our stack is empty and we did not reach the end node.
            return False

        return bfs()
```
## Complexity Analysis
- Time complexity : 
    - DFS Time Complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.
        - Visiting Each Vertex (V): In a DFS traversal, every vertex in the graph is visited exactly once. This is because DFS explores as far as possible along each branch before backtracking. Therefore, the time complexity associated with visiting each vertex is O(V).
        - Exploring Each Edge (E): For each vertex visited, DFS explores all its adjacent edges to find unvisited vertices. In the worst case, where the graph is dense (i.e., every vertex is connected to every other vertex), each edge will be explored once. Therefore, the time complexity associated with exploring each edge is O(E).

    - BFS Time Complexity - O(V + E), where V is the number of vertices and E is the number of edges in the graph.

- Space complexity : 
    - DFS Space Complexity - O(V), where V is the number of vertices in the graph. This accounts for the space required for the ```visited``` set and the call ```stack``` in the worst case.

    - BFS Space Complexity - O(V), where V is the number of vertices in the graph. This accounts for the space required for the ```visited``` set and the ```queue``` in the worst case.