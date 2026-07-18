class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        province = 0

        def dfs(c):
            for x in range(n):
                if isConnected[c][x] == 1 and x not in visited:
                    visited.add(x)
                    dfs(x)
            
        
        for x in range(n):
            if x not in visited:
                province += 1
                visited.add(x)
                dfs(x)

        
        return province
                    
            