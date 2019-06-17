class Solution:
    def isValid(self, s: str) -> bool:
        open = "({["
        close = ")}]"

        temp = 0
        for item in s:
            if open.__contains__(item):
               temp += 1
            elif close.__contains__(item):
                temp -= 1

        if temp % 2 == 0:
            return True
        else:
            return False



s = Solution()
temp = ")((}}[][][()]{{"
print(s.isValid(temp))