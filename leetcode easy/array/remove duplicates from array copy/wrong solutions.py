from ast import List


# nums = [1,1,2,2,3,4,5]
# arr = [1,1,2,2,3,4,5]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            element = nums[i]
            next_element = element+1
            if next_element in nums:
                nums.insert(i+1, next_element)
                
        heightest_number_index = nums.index(max(nums))
        del nums[heightest_number_index+1:]
        
        
        # arr = nums[:heightest_number_index+1]
            
            
            
            # try:
            #     element = nums[i]
            #     nums.remove(element)
            #     if element in nums:
            #         idx = nums.index(element)
            #         nums.pop(idx)
            #         nums.insert(idx,element)
            #     else:
            #         nums.insert(i,element)
            # except:
            #     pass
        
        # for i in range(len(nums)):
        #     element = nums[i]
        #     nums.remove(element)
        #     if element in nums:
        #         nums.remove(element)
        # for i in range(len(nums)):
        #     try:
        #         element = nums[i]
        #         for j in range(i+1, len(nums)-1):
        #             if element+1 != nums[i+1]:
        #                 nums.remove(nums[i+1])
        #     except:pass
        
        
#         for i in range(len(nums)-1):
#             element = nums[i]
#             # if element in nums[i+1:]:
                
#             nums.pop(i)
#             # for j in range(length_of_array):
#             if element in nums:
#                 # nums.remove(element)
#                 i+1
#             else:
#                 nums.insert(i,element)
#         return len(nums)
            
    
        #     try:
        #         element = nums[i]
        #         if element == nums[i+1]:
        #             nums.pop(i+1)
        #     except:pass
        #     k = len(nums)
        # return k




class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums)):
            element = nums[i]
            next_element = element+1
            if next_element in nums:
                nums.insert(i+1, next_element)
        heightest_number_index = nums.index(max(nums))
        arr = nums[:heightest_number_index+1]
        print (arr)
        print (heightest_number_index)
    
obj = Solution()
obj.removeDuplicates(nums)

nums =[0,0,1,1,1,2,2,3,3,4]
for i in range(len(arr)):
    # print(i)
    print(arr[i])

def removeDuplicates():
    for i in range(len(nums)):
        try:
            element = nums[i]
            nums.remove(element)
            if element in nums:
                idx = nums.index(element)
                nums.pop(idx)
                nums.insert(idx,element)
            else:
                nums.insert(i,element)
        except:
            pass
    print(nums)
    
removeDuplicates()