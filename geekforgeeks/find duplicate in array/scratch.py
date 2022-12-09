# just figuring out the solution

arr = [1,2,3,3,5]
duplicates = []
for i in range(len(arr)-1):
    pivot = arr[i]
    arr.pop(i)
    duplicate_exist = pivot in arr
    if duplicate_exist:
        duplicates.append(pivot)
if duplicates == []:
    duplicates.append(-1)
print(duplicates)
