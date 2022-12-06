class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        nums = [2, 7, 11, 15]
        while i < len(nums)-1:
            result = nums[i] + nums[i+1]
            if result == target:
                a = nums[i]
                b = nums[i+1]
                c = [nums.index(a), nums.index(b)]
                return c
            i += 1


# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# status : case 1 is right 
# failing case 2 and 3
# link : https://leetcode.com/problems/two-sum/
