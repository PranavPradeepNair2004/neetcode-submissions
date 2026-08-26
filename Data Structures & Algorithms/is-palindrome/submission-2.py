class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        inverse_pal= s[::-1]
        if s==inverse_pal:
         return True
        else:
         return False      