class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            new_list = nums.copy()
            new_list.pop(x)
            if new_list == sorted(set(new_list)):
                return True
        
        return False