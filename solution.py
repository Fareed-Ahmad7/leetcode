class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        sum = 0
        while i < len(nums):
            sum = nums[i]+sum
            nums[i] = sum
            i = i + 1
        return nums
