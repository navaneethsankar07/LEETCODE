class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(node):
            for x in range(n):
                if isConnected[node][x] == 1 and x not in visited:
                    visited.add(x)
                    dfs(x)
        
        provinces = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
        
        return provinces