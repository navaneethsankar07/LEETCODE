class Solution:
    def trimMean(self, arr: List[int]) -> float:
        percentage = int(len(arr) * 5/100)
        for x in range(percentage):
            arr.remove(min(arr))
            arr.remove(max(arr))
        return sum(arr)/len(arr)