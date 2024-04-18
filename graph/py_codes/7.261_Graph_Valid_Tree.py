class Solution:
    def validTree(self, n: int, edges) -> bool:
        adjacency = {node:[] for node in range(n)}
        for neighbor1, neighbor2 in edges:
            adjacency[neighbor1].append(neighbor2)
            adjacency[neighbor2].append(neighbor1)

        visited = set()

        def dfs(node, previous):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjacency[node]:
                if previous == neighbor:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)