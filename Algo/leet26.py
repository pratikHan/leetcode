import time


class Solution:
    def removeDuplicates(self,nums) :
        
        s_time = time.time()
        
        dif_num = 1
        if nums == []:
            return 0
        
        nums.sort()

        for i in range(len(nums)):
            if (i + 1 < len(nums)):
                if nums[i] < nums[i + 1]:
                    nums[dif_num] = nums[i + 1]
                    dif_num += 1

        print "Execution Time :" ,(time.time() - s_time)
        return dif_num


c = Solution()
a = [8,9,2,4,11,2]
f = c.removeDuplicates(a)
print(f)

