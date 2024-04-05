
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        oldToNew = {}

        def dfs(node):
            # visited
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
    
# nodes = [[2,4],[1,3],[2,4],[1,3]]
# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Define neighbors
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_graph = solution.cloneGraph(node1)

# Function to print graph nodes and their neighbors
def print_graph(node, visited):
    if not node or node in visited:
        return
    visited.add(node)
    print(f"Node {node.val} -> {[n.val for n in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

# Print original and cloned graphs
print("Original Graph:")
print_graph(node1, set())
print("\nCloned Graph:")
print_graph(cloned_graph, set())