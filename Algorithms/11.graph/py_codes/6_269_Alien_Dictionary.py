class Solution:
    def alienOrder(self, words) -> str:
        # Init
        # graph
        adjacency = {character:set() for word in words for character in word}
        # visited
        visited = {}
        # result list -> string
        result = []

        # Create graph: Check all pairs of words to check for prefix relationships
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            minLength = min(len(word1), len(word2))
            # Check the first part of word 1 and 2 is the same and word 1 is lengthier than word 2, it is invalid solution
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""

            for j in range(minLength):
                # If the first character of word1 and word2 differs, add to graph
                if word1[j] != word2[j]:
                    adjacency[word1[j]].add(word2[j])
                    break

        # DFS function: The DFS is used to detect cycles in the graph
        # False: visited; True: in current path (helpful for cycles)
        def dfs(character):
            # There is a cycle and it has seen 2 times
            if character in visited:
                return visited[character]

            visited[character] = True

            # Check neighbors
            for neighbor in adjacency[character]:
                # check neighbors for a cycle
                if dfs(neighbor):
                    return True

            # the node is visited
            visited[character] = False
            result.append(character)
        
        # Run Main part
        for node in adjacency:
            # Check if there is any cycle
            if dfs(node):
                return ""
        result.reverse()
        return "".join(result)