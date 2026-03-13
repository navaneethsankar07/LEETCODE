class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late =0
        for x in s:
            if x == 'A':
                absent += 1
                late = 0
                if absent > 1:
                    return False            
            elif x == 'L':
                late +=1
                if late > 2:
                    return False
            else:
                late = 0
        
        return True
            
        