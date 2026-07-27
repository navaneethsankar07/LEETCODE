class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            new_nums = []
            for x in range(len(nums)//2):
                if x % 2 == 0:
                    new_nums.append(min(nums[2 * x], nums[2 * x + 1]))
                else:
                    new_nums.append(max(nums[2 * x],nums[2 * x + 1]))
                
                
            nums = new_nums

        return nums[0]