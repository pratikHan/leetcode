class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #temp: str = ""

        if len(strs) == 0:
            return ""

        res = strs[0]

        for i in range(len(strs)):
            res = self.lcp(res, strs[i])
        return res



    def lcp(self,s1,s2):

        t : str = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return t
            else:
                t += s1[i]
        return t


        

s = Solution()
strs = ["aca","cba"]
print(s.longestCommonPrefix(strs))