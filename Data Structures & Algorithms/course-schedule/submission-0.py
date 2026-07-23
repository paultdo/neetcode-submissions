class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        prereqMap = defaultdict(list)

        for pair in prerequisites:
            prereqMap[pair[0]].append(pair[1])
        
        def dfs(course):
            if course in path:
                return False
            
            path.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


            

            



