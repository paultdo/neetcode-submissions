class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = defaultdict(list)
        path = set()
        visited = set()
        res = []
        isCycle = False
        for pair in prerequisites:
            prereqMap[pair[0]].append(pair[1])

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                isCycle = True
        
        return res if not isCycle else []