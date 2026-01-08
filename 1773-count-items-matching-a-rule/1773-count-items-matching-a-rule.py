class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        item_format = {
            'type':0,
            'color':1,
            'name':2
        }
        item = item_format[ruleKey]
        count = 0
        print(item)
        for x in items:
            if x[item] == ruleValue:
                count += 1
        return count