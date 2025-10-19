class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counter = 0
        index = 0
        for x in mat:
            val = x.count(1)
            if val>counter:
                counter = val
                index = mat.index(x)
        return [index,counter]