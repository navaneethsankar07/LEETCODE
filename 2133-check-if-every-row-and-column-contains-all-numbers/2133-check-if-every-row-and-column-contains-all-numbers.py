class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        nums = set([x for x in range(1,len(matrix)+1)])
        return all(nums == set(x) for x in matrix + list(zip(*matrix)))