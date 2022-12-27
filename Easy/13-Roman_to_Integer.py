# 
# Runtime: 
# Memory: 

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = {
            "I": 1,
            "V": 2,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        print(romanToInteger)

solve = Solution()
solve.romanToInt("III")