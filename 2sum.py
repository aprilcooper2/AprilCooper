#Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i in range(len(nums)):
            if nums[i] in numMap:
                numMap[nums[i]] += i
            else:
                numMap[nums[i]] = i
                
        for i in range(len(nums)):
            secondNum = target - nums[i]
            if secondNum in numMap and numMap[secondNum] != i:
                if secondNum == nums[i]:
                    return [i, numMap[secondNum] - i]
                else:
                    return [i, numMap[secondNum]]
                    
                    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = 0
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                low = hashmap[target - nums[i]]
                high = i
            else:
                hashmap[nums[i]] = i
        return [low,high]
