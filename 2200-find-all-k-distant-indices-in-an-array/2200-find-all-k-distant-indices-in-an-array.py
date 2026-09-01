class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        index = []
        n = len(nums)

        for x in range(n):
            for y in range(n):
                if nums[y] == key and abs(x - y) <= k:
                    index.append(x)
                    break
        return index