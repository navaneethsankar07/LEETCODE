from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1
        
        q = deque(i for i in range(numCourses) if degree[i] == 0)

        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for nxt in graph[node]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        

        return numCourses == visited