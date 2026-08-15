class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        boxes = 0

        capacity.sort()
        total_apple = sum(apple)
        x = len(capacity)-1

        while total_apple > 0:
            print(x)
            total_apple -= capacity[x]
            boxes += 1
            x -= 1
        
        return boxes