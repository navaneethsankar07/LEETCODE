class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        for x in range(1,len(arr)):
            if abs(arr[x] - arr[x-1]) > 1:
                arr[x] = arr[x-1] + 1

        return max(arr)
