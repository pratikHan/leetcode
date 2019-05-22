class Solution(object):

    def isPalidrome(self, x):
        num = 0
        t = x
        if x<0:
            return False
        while x>=1:
            num = num * 10 + int(x % 10)
            x = int(x/10)

        if num == t:
            return  True
        else:
            return False




c = Solution()
print(c.isPalidrome(20))