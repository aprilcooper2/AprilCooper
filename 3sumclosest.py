#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result, gap = 0, sys.maxint
        
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while (l < r):
                sumNum = nums[i] + nums[l] + nums[r]
                if sumNum == target:
                    return sumNum
                if sumNum > target:
                    if gap > sumNum - target:
                        gap = sumNum - target
                        result = sumNum
                    r -= 1
                else:
                    if gap > target - sumNum:
                        gap = target - sumNum
                        result = sumNum
                    l += 1
        return result
