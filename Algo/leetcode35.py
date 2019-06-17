class Solution(object):

    # 1,3,11,17,20 target = 10



    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        mid = len(nums)/2
        found = False


        while first <= last and not found:

            mid = int((first + last)/2)


            if nums[mid] == target:
                found = True
                return mid

            if nums[mid] > target and nums[mid -1] < target:
                return mid
            elif target > nums[last]:
                return last + 1
            elif target < nums[first]:
                return first


            if target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

s = Solution()
alist = [1]
print(s.searchInsert(alist,2))


