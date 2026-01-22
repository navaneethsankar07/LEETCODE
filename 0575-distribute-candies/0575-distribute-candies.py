class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique = set(candyType)
        return min(len(candyType)//2,len(unique))