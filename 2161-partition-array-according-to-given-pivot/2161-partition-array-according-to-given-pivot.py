class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        equals = []
        for x in range(len(nums)):
            if nums[x] < pivot:
                left.append(nums[x])
            elif nums[x] > pivot:
                right.append(nums[x])
            else:
                equals.append(nums[x])
        
        equals+=right
        left+=equals
        return left