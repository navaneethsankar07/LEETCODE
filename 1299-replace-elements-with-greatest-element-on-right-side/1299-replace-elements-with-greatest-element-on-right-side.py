class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = -1
        for x in range(len(arr)-1,-1,-1):
            temp = arr[x]
            arr[x] = num
            num = max(num,temp)
        
        return arr