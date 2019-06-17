## in a given list of numbers find combination of 3 numbers whos sum is 0
"""
eg Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        temp = []

        if (len(nums) >= 3) and (nums[0] == nums[len(nums) - 1]) and (nums[0] == 0):
            return [[0, 0, 0]]

        for index in range(len(nums) - 1):
            print("FOR:")
            first = index + 1
            last = len(nums) - 1

            while first < last:
                print("WHILE:")
                currentsum = nums[first] + nums[last] + nums[index]
                print(temp)
                print(currentsum)

                if currentsum == 0:
                    print(index, first, last)
                    if index not in temp or first not in temp or last not in temp:
                        print("donw")
                        results.append([nums[index], nums[last], nums[first]])

                        temp.append(index)
                        temp.append(last)
                        temp.append(first)

                    first += 1
                    last -= 1

                elif currentsum < 0:
                    first += 1
                else:
                    last -= 1



        return results

s = Solution()
l = [-1, 0, 1,2,-1,-4]
print(s.threeSum(l))
