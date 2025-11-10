class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        index = -1
        for x in range(index+1,length):
            if nums[x] == 1:
                if index != -1 and (x-index-1) < k:
                    return False
                index = x
        return True 

