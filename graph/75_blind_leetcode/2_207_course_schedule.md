# LeetCode Problem 200: [Course Schedule](https://leetcode.com/problems/course-schedule/description/)
## Problem Description
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.
## Solution Approaches
### DFS Algorithm
Algorithm Pattern: Course Schedule using Topological Sort

1. Initialization
    - Purpose: Prepare the necessary data structures for the algorithm.
    - Steps:
        - Create a dictionary ```preMap``` to map each course to its prerequisites.
        - Initialize an empty set ```visited``` to keep track of visited courses.
2. DFS Function
    - Purpose: Perform a depth-first search on the course graph to check for cycles.
    - Steps:
        - Define a nested function ```dfs``` that takes a course as input.
        - Check if the course has already been visited. If so, return False to indicate a cycle.
        - Mark the course as visited.
        - For each prerequisite of the course, recursively call ```dfs```. If any call returns ```False```, return ```False``` to indicate a cycle.
        - After visiting all prerequisites, remove the course from the visited set to allow it to be ```visited``` again in a different path (if necessary).
        - Return ```True``` to indicate that the course can be taken without forming a cycle.
3. Main Function
    - Purpose: Determine if it's possible to finish all courses.
    - Steps:
        - Iterate over all courses. For each course, call the ```dfs``` function. If any call returns ```False```, return ```False``` to indicate that it's not possible to finish all courses.
        - If all courses can be visited without forming a cycle, return ```True```.
## Example Description

## Python Code
```python
class Solution:
    def dfs(self, crs, visited, preMap):
        # Check if crs is visited, it is imposible to loop back to crs and 2 crs
        if crs in visited:
            return False
        if preMap[crs] == []:
            return True

        # crs is visited
        visited.add(crs)

        for pre in preMap[crs]:
            if not self.dfs(pre, visited, preMap): return False
        visited.remove(crs)
        preMap[crs] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        for crs in range(numCourses):
            if not self.dfs(crs, visited, preMap): return False
        return True
```
## Complexity Analysis
- Time complexity : O(N + E), where N is the number of courses and E is the number of prerequisites. This is because each course and prerequisite is visited exactly once.

- Space complexity : O(N), where N is the number of courses. This is due to the space required for the ```preMap``` dictionary and the ```visited``` set.