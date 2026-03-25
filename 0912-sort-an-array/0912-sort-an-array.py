class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for x in range(1,len(nums)):
            key = nums[x]
            j = x - 1

            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = key
        
        return nums