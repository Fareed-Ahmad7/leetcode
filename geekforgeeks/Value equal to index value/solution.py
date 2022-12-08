#User function Template for python3
class Solution:

	def valueEqualToIndex(self, arr, n):
    
        arr1 = []
        for i in range(len(arr)):
            element = arr[i]
            index = i+1
            if element == index:
                arr1.append(element)
        return arr1
