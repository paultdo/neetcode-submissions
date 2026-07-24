class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adjList = defaultdict(list)
        count = 0
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)
        

        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        
        return count


