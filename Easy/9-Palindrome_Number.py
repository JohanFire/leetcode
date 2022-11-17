# Accepted
# Runtime: 91 ms
# Memory: 13.9 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False