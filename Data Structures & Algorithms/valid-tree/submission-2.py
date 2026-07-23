class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor != parent and not dfs(neighbor, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n