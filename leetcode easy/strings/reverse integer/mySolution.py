x = 123


class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)
        print(string_x[::-1])


class Solution2:
    def reverse(self, x: int) -> int:
        string_x = str(x)
        if '-' in string_x:
            print('-')
        for i in range(len(string_x)):
            if string_x[i] != "-" and string_x[i] != "0":
                print(string_x[len(string_x)-1-i])

obj = Solution()
obj.reverse(x)

print("solution2")
obj2 = Solution2()
obj2.reverse(x)


