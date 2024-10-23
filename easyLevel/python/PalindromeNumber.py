class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = x
        reversed_num = 0
        
        if x < 0:
            return False
        
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return reversed_num == forward