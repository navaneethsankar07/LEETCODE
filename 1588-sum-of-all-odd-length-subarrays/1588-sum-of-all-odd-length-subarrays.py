class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        length = len(arr)
        for i in range(length+1):
            if i % 2 != 0:
                for x in range(length - i + 1):
                    total += sum(arr[x:x+i])
                
        return total
        