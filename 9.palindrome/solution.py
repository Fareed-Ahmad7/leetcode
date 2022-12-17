class Solution:
    def isPalindrome(self, x: int) -> bool:
            str_x = str(x)
            reversed_number = str_x[::-1]
            if str_x == reversed_number:
                return True
            else:
                return False



link : "https: // leetcode.com/problems/palindrome-number/submissions/861248041/"
status : accepted