class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        seen = set()
        while right < len(nums):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            right += 1
            if right - left > k:
                seen.remove(nums[left])
                left += 1
        return False
