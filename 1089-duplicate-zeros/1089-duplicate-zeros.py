class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        length = len(arr)
        while i<length:
            if arr[i] == 0:
                arr.insert(i+1,0)
                i +=1
                arr.pop()
            i+=1
        
        