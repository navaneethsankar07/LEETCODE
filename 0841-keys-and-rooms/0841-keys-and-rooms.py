class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        keys = [0]

        while keys:
            key = keys.pop()

            for x in rooms[key]:
                if x not in visited:
                    visited.add(x)
                    keys.append(x)
        print(visited)
        return len(visited) == len(rooms)