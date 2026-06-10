class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict_ = dict(items1)

        for v, w in items2:
            if v in dict_:
                dict_[v] += w
            else:
                dict_[v] = w
        return sorted(dict_.items())