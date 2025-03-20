class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currentSum = 0
        minLength = float('inf')

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                minLength = min(minLength, right - left + 1)
                currentSum -=nums[left]
                left += 1

        return minLength if minLength != float('inf') else 0