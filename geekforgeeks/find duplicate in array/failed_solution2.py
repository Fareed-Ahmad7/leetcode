arr = [0, 3, 3, 3, 1, 3, 25, 5, 25, 25]
arr.sort()
duplicates = []
for i in range(len(arr)-1):
    j = i+1
    element = arr[i]
    next_element = arr[j]
    element_exist = element in duplicates
    if element == next_element and element_exist is False:
        duplicates.append(element)
if duplicates == []:
    duplicates.append(-1)
print(duplicates)

# time limit exceed!