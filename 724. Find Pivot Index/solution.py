class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)  # takes o(n) of time to sum the the all numbers
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

#  status : Accepted
# link : https://leetcode.com/problems/find-pivot-index/
