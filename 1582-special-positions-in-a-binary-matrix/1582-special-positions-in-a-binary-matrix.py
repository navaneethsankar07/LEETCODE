class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        row = [0] * m
        col = [0] * n

        for x in range(m):
            for y in range(n):
                if mat[x][y] == 1:
                    row[x] += 1
                    col[y] += 1
        
        for i in range(m):
            if row[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1 and col[j] == 1:
                        count += 1
        
        return count