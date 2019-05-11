import time
# find the longest substring from a given string
# a= abcabcabc length =3
#a = bbbbb length = 1
# a = pwwkew len = 3

start = time.time()
class Solution(object):
    def longestsub(self, s1):
        count = 0
        x = []
        res = []


        for t in s1:
            if t not in x:
                x.append(t)
                count += 1
            else:
                if t != len(s1):
                   # count +=1
                    x = []
                    x.append(t)
                    res.append(count)
                    count = 1


        return len(s1) if res == [] else max(res)

c = Solution()
j = "abcabcabc"
print("final :")
print(c.longestsub(j))

end = time.time()
fin = end - start

print("Exec time :")
print(fin)