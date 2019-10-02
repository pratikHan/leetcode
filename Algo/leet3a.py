class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype : int
        """
        temp = ""
        m = 0
        asa = []

        if s == "":
            return 0

        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
                m = len(temp)
            else:
                m = max(m, len(temp))
                print( m)
                temp = ""
                temp += s[i]

        return 1 if m == 0 else m


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
