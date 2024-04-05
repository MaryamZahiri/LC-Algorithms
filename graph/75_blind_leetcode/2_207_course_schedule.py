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

    def canFinish(self, numCourses, prerequisites) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        for crs in range(numCourses):
            if not self.dfs(crs, visited, preMap): return False
        return True
    
numCourses = 2
prerequisites = [[1,0]]
solution = Solution()
course_schedule = solution.canFinish(numCourses, prerequisites)
print("Can we finish the courses: ", course_schedule)