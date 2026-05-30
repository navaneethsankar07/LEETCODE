class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        
        while mainTank > 0:
            if mainTank >= 5:
                res += 50
                mainTank -= 5
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                res += 10 * mainTank
                break
        
        return res