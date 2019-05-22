class Solution(object):

    def reversex(self, num):

        rev = 0


        while num != 0:
            rem = int(num % 10)
            print(rem)
            rev = (rev * 10) + rem
            num = int(num/10)

        return rev

q = Solution()
print(q.reversex(-11))