class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i:[] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)

            for x in graph[node]:
                if x not in visited:
                    if dfs(x):
                        return True
            
            return False
        
        return dfs(source)