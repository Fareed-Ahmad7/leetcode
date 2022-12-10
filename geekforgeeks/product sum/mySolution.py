#User function Template for python3
class Solution:
    def countDigits(self, a, b):
        product = a*b
        string = str(product)
        negative_symbol_exist = '-' in string
        num_of_digits = 0
        if negative_symbol_exist:
            num_of_digits -= 1
        for i in string:
            num_of_digits += 1
        return num_of_digits


# status: Accepted!