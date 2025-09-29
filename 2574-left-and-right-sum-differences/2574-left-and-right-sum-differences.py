class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = 0
        rightsum = 0
        length = len(nums)
        answer = []
        for x in range(length):
            if x == 0:
                leftsum = 0
                rightsum = sum(nums[x+1:])
            elif x == length-1:
                rightsum = 0
                leftsum = sum(nums[:x])
            else:
                leftsum = sum(nums[:x])
                rightsum = sum(nums[x+1:])
            answer.append(abs(leftsum-rightsum))
        return answer