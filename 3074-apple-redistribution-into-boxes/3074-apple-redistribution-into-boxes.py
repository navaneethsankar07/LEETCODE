class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        for i, val in enumerate(capacity, 1):
            total -= val

            if total <= 0:
                return i
