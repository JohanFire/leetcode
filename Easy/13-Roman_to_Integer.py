# 
# Runtime: 
# Memory: 

class Solution:
    def romanToInt(self, s: str) -> int:
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        
        vM = s / M
        mResiduo = s % 100
        print(vM)
        print(mResiduo)

solve = Solution()
solve.romanToInt("III")